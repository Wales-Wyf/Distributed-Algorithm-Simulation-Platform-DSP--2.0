import copy
import time
def taskFunction(self,id,adjDirection,datalist):
    #init 
    parent_direction = copy.deepcopy(datalist[0])
    child_direction = copy.deepcopy(datalist[1])
    J = copy.deepcopy(datalist[2])
    End_Counter = len(child_direction)
    data_base = [0,False,False,J]  # 邻居方向,COMPUTE, VALUE, J
    data = []
    if len(parent_direction):
        for i in range(len(parent_direction)):
            data_base_temp = [0,False,False,J]  
            data_base_temp[0] = parent_direction[i]
            data.append(data_base_temp)

    if len(child_direction):
        for i in range(len(child_direction)):
            data_base_temp = [0,False,False,J]  
            data_base_temp[0] = child_direction[i]
            data.append(data_base_temp)

    if id == 1:
        for i in range(len(data)):
            data[i][1] = True    #COMPUTE            

    for m in range(10):
        time.sleep(0.1)
        for i in range(len(data)):
            if data[i][0] != 0:
                self.sendDataToDirection(data[i][0],data[i][1:4])
        self.syncNode()
        adjData_fb = copy.deepcopy(self.adjData)
        adjDirection_fb = adjDirection

        for i in range(len(data)):
            data[i][1] = False    #COMPUTE
            data[i][2] = False    #VALUE

        for i in range(len(adjData_fb)):
            if adjData_fb[i]:
                if adjData_fb[i][0] == True:   #COMPUTE
                    if len(child_direction):
                        for k in range(len(data)):
                            if data[k][0] != adjDirection_fb[i]:
                                data[k][1] = True    #COMPUTE
                    else:
                        for k in range(len(data)):
                            if data[k][0] == adjDirection_fb[i]:
                                data[k][2] = True    #VALUE                   

                if  adjData_fb[i][1] == True:  #VALUE 
                    J = J + adjData_fb[i][2]
                    for k in range(len(data)):
                        data[k][3] = J       
                        
                    End_Counter = End_Counter - 1
                    if End_Counter == 0:
                        for k in range(len(data)):
                            if data[k][0] == parent_direction[0]:
                                data[k][1] = False   #COMPUTE
                                data[k][2] = True    #VALUE 

        self.sendUDP("第" + str(m+1) + "步完成 计算结果为："+str(J))

    value = J
    return value