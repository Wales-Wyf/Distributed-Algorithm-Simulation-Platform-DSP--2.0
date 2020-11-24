import copy
import time 

def taskFunction(self,id,adjDirection,datalist):
    # init 
    # 生成树节点标识
    Flag = False  
    # 用于判断计算是否结束的END计数器
    End_Counter = 0
    # 父节点方向
    parentdirection = []
    # 子节点方向
    childdirection = []
    # END计数器初始化为邻居数量
    End_Counter = len(adjDirection)
    # 与邻居通信的数据格式，分别为邻居的方向、BFS信号、END信号
    data_base = [0,False,0] 
    # 本地给不同邻居的数据数组
    data = []

    # 初始化data
    for i in range(len(adjDirection)):
        data_base_temp = [0,False,0]
        data_base_temp[0] = adjDirection[i]
        data.append(data_base_temp)

    # id为1的为发起节点
    if id == 1:
        Flag = True
        parentdirection.append(0)  # 假定一个0方向，父节点方向为0的即为根节点/发起节点
        for i in range(len(data)):
            data[i][1] = True      # 给每个邻居发送BFS信号  

    # 循环次数为网络规模的2倍，5  *2 = 10
    for m in range(10):
        time.sleep(0.1)                                        # 异步通信函数前sleep一段时间防止通信数据覆盖写入
        for i in range(len(data)):
            self.sendDataToDirection(data[i][0],data[i][1:])   # 只传给邻居BFS和END信号
        self.syncNode()                                        # 同步异步通信函数
        adjData_fb = copy.deepcopy(self.adjData)               # 获取邻居传输的数据
        adjDirection_fb = adjDirection                         # 获取邻居的方向数组

        # 清空BFS、END信号
        for i in range(len(data)):
            data[i][1] = False
            data[i][2] = 0

        # 如果END计数器不为0
        if  End_Counter != 0:
            for i in range(len(adjData_fb)):
                # 如果邻居传来BFS信号
                if adjData_fb[i][0] == True:    
                    # 如果本节点没有加入宽度优先生成树中             
                    if Flag == False:
                        Flag = True
                        parentdirection.append(adjDirection_fb[i])  #将邻居方向加入父节点方向
                        # 向其他邻居广播BFS信号
                        for j in range(len(data)):
                            if data[j][0] != adjDirection_fb[i]:
                                data[j][1] = True
                    End_Counter = End_Counter - 1     

                # 如果邻居传来END信号
                if  adjData_fb[i][1] > 0:
                    End_Counter = End_Counter - 1
                    # END = 2 说明是该节点的子节点，将邻居方向加入父节点方向数组
                    if adjData_fb[i][1] == 2: 
                        childdirection.append(adjDirection_fb[i])

            # 如果本轮END计数器减为0
            if End_Counter == 0:
                for i in range(len(data)):
                    data[i][1] = False
                    # 给父节点方向的邻居发送END = 2
                    if data[i][0] == parentdirection[0]:
                        data[i][2] = 2
                    # 给其他邻居发送END = 1
                    else:
                        data[i][2] = 1
        self.sendUDP("第" + str(m+1) + "步完成")

    # 返回父节点方向、子节点方向
    value = [parentdirection,childdirection]
    return value