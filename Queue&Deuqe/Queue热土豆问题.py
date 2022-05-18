class Queue:                   #队首在list最后，队尾在list最前
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

#热土豆问题（约瑟夫问题）：一堆人坐一圈，报数1-7，报到7的被死
def hotPotato(namelist,num):   #num 为传递次数
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)  #把人放到队列里
    while simqueue.size() > 1:  #直到剩下最后一个人
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  #把队首的人放到队尾
        simqueue.dequeue()      #把队首的人干死
    return simqueue.dequeue()   #把最后一个人输出

print("最后活下来的人是：",hotPotato(["Bill","David","Susan","Jane","王业强","Brad"],6))

