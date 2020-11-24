# encoding: utf-8
import topology
import json

js = []
tp = topology.topology()
IP = tp[0]
PORT = tp[1]
adjID = tp[2]
datalist = tp[3]

for i in range(len(IP)):
    tmp = {}
    tmp["ID"] = i+1
    tmp["IP"] = IP[i]
    tmp["PORT"] = PORT[i]
    tmp["adjID"] = adjID[i]
    tmp["datalist"] = datalist[i]
    js.append(tmp)

try:
    a = json.dumps(js)
except Exception:
    print "JSON格式错误"
else:
    print a