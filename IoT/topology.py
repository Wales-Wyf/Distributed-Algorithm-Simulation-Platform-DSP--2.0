# coding=utf-8
import copy
import socket

def topology():
    # 确定立方体结构
    m = 2
    n = 5
    l = 5
    co = []
    adjID = []
    IP = []
    PORT = []
    datalist = []
    # localIP = socket.gethostbyname(socket.gethostname())
    localIP = "localhost"
    # 定义每个节点IP与端口(PORT[0]~PORT[5]为通信端口，PORT[6]为交互端口)
    for i in range(m*n*l):

        IP.append(localIP)
        PORT.append([])
        datalist.append([])
        for j in range(7):
            PORT[i].append(10000+7*i+j)

    # 确定立方体结构每个节点的邻接节点与对应路由关系
    for i in range(m*n*l):
        co.append([i/(m*n),(i%(m*n))/n,(i%(m*n))%n])
    for i in range(m*n*l):
        tmp0 = copy.copy(co[i])
        tmp = []
        for j in range(3):
            tmp1 = copy.copy(tmp0)
            tmp2 = copy.copy(tmp0)
            tmp1[2-j] += 1
            tmp2[2-j] -= 1
            if tmp1 in co:
                tmp.append(co.index(tmp1))
            if tmp2 in co:
                tmp.append(co.index(tmp2))
        adjID.append(tmp)
    for i in range(len(adjID)):
        for j in range(len(adjID[i])):
            adjID[i][j] += 1

    # 返回[邻接节点ID数组，路由表数组，IP数组，端口数组]，其中数组的含义是涵盖了全部n个节点的相应信息
    return [IP, PORT, adjID, datalist]


