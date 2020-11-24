# import需求模块
import random
# 用户自定义函数区
"""
用户编码区域
"""

# 定义算法主函数taskFunction(self,id,adjDirection,datalist)，四个形参分别为节点类，节点ID，节点邻居对应的方向以及初始化时键入的数据
def taskFunction(self, id, adjDirection, datalist):
    temp = round(random.uniform(0,30))
    self.sendUDP("初始温度为：" + str(temp))
    maxtemp = temp
    for m in range(10):
        data = self.transmitData(maxtemp)
        adjDirection = data[0]
        adjData = data[1]
        for i in range(len(adjData)):
            if adjData[i] > maxtemp:
                maxtemp = adjData[i]
        self.sendUDP("第" + str(m+1) + "步完成")
    value = maxtemp
    # value为返回值，可为JSON能解析的任意格式
    return value