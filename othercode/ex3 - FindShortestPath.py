import copy

def taskFunction(self,id,adjDirection,datalist):

    # init 
    parentdirection = 0
    Dn = float('inf')
    cost = copy.deepcopy(datalist)  
    #通过宽度优先生成树等方法求得网络节点总数
    N = 5              
    
    if id == 1:
        Dn = 0
    self.sendUDP(str(Dn))

    for m in range(N):
        feedback = self.transmitData(Dn)
        adjDirection_fb = copy.deepcopy(feedback[0])
        adjData_fb = copy.deepcopy(feedback[1])

        minidist = Dn
        minidist_direction = 0
        for i in range(len(adjDirection_fb)):
            for j in range(len(adjDirection)):
                if adjDirection_fb[i] == adjDirection[j]:
                    if adjData_fb[i] + cost[j] < minidist:
                        minidist = adjData_fb[i] + cost[j]
                        minidist_direction = adjDirection_fb[i]
        if minidist < Dn:
            Dn = minidist
            parentdirection = minidist_direction                

        self.sendUDP("第" + str(m+1) + "步完成 最短路径为" + str(Dn))
    
    value = [parentdirection, Dn]
  
    return value