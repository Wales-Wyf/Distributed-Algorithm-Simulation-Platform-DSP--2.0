import copy

def taskFunction(self,id,adjDirection,datalist):
    n = copy.deepcopy(datalist[0])
    a = copy.deepcopy(datalist[n])
    b = copy.deepcopy(datalist[-1])
    ann = copy.deepcopy(datalist[1:-1])
    x = 0.0
    K = 5
    data = [n, x]

    for m in range(5):
        feedback = self.transmitData(data)   
        adjData = copy.deepcopy(feedback[1])  
        t = 0
        for i in range(len(adjData)):
            t = t - adjData[i][1] * ann[adjData[i][0] - 1]
        x = (b + t) / a
        data = [n, x]

        self.sendUDP("第" + str(m+1) + "步完成 计算结果为：" + str(x))
    value = x
    return value