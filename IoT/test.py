# Copyright 2020 Center for Intelligent and Networked Systems.
# This program is distributed under the Apache license 2.0.
# Supported by National Key Research and Development Project of China (No. 2017YFC0704100 entitled New generation intelligent building platform techniques) and the National Natural Science Foundation of China (No. 61425027), the 111 International Collaboration Program of China under Grant BP2018006.

import server
import sys
import codecs
import json
import os
import socket

if __name__ == '__main__':
    IP = []
    PORT = []
    ID = []
    adjID = []
    datalist = []
    adjDirection = []
    localIP = socket.gethostbyname(socket.gethostname())
    path = os.getcwd() + "\\IoT\\topology.txt"
    # path = os.getcwd() + "\\topology.txt"
    text = codecs.open(path, 'r', 'utf-8').read()
    js = json.loads(text)
    for ele in js:
        if "ID" in ele:
            ID.append(ele["ID"])
            if ele["IP"] == 'localhost':
                IP.append(localIP)
            else:
                IP.append(ele["IP"])
            PORT.append(ele["PORT"])
            adjID.append(ele["adjID"])
            adjDirection.append(ele["adjDirection"])
            datalist.append(ele["datalist"])

    # wait to insert
    path2 = os.getcwd() + "\\IoT\\debug.txt"
    # path2 = os.getcwd() + "\\debug.txt"
    debuglist = []
    debugmode_flag = 0
    with open( path2, 'r' ) as f:
        for line in f.readlines():  
            line=line.strip('\n')  
            debuglist.append(line)
    print (debuglist)


    if "start in debug mode" in debuglist:
        debugmode_flag = 1
    if debugmode_flag:
        debuglist.pop()
        
    user = debuglist.pop(0)
    passwd = debuglist.pop(0)
    databasename = debuglist.pop(0)
    tablenamePrefix = debuglist.pop(0)

    debuglist[0] = debuglist[0].strip(" ")
    observelist = []
    if len(debuglist) and debuglist != [""]:
        observelist = debuglist

    order = int(sys.argv[1]) - 1
    selfID = ID[order]
    selfAdjID = adjID[order]
    selfAdjDirection = adjDirection[order]
    selfIP = IP[order]
    selfPORT = PORT[order]
    selfDatalist = datalist[order]
    selfIPList = []
    n = len(IP)
    for i in range(len(selfAdjID)):
        selfIPList.append([])
        direction = selfAdjDirection[i] - 1
        selfIPList[i].append(selfIP)
        selfIPList[i].append(selfPORT[direction])
        for j in range(n):
            if ID[j] == selfAdjID[i]:
                selfIPList[i].append(IP[j])
                for k in range(len(adjID[j])):
                    if adjID[j][k] == selfID:
                        selfIPList[i].append(PORT[j][adjDirection[j][k]-1])
                        break
                selfIPList[i].append(ID[j])
                break
    print(selfIPList)
    # adjPort = []
    # n = len(IP)
    # totalIPlist = []
    # for i in range(n):
    #     adjPort.append(0)
    #     totalIPlist.append([])
    #     for j in range(6):
    #         totalIPlist[i].append([])
    # print (len(totalIPlist))
    # for i in range(n):
    #     for adj1 in adjID[i]:
    #         adj = adj1 - 1
    #         if i < adj:
    #             totalIPlist[i][adjPort[i]] = [IP[i], PORT[i][adjPort[i]], IP[adj], PORT[adj][adjPort[adj]], adj + 1]
    #             totalIPlist[adj][adjPort[adj]] = [IP[adj], PORT[adj][adjPort[adj]], IP[i], PORT[i][adjPort[i]], i + 1]
    #             adjPort[i] += 1
    #             adjPort[adj] += 1
    #
    # print(totalIPlist[0])
    # print(adjID)
    # print(adjDirection)
    sensor = server.Sensor(selfID, selfAdjID, selfAdjDirection, selfIPList, selfIP, selfPORT, selfDatalist, tablenamePrefix = tablenamePrefix, observelist = observelist, user = user, passwd = passwd,databasename = databasename, debugmode_flag = debugmode_flag)
    sensor.run()