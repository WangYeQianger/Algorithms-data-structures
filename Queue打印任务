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

#打印任务
import random

class Printer:   #打印机定义
    def __init__(self,ppm):
        self.pagerate = ppm       #打印速度
        self.currentTask = None   #打印任务 None为空闲
        self.timeRemaining = 0    #任务倒计时
    def tick(self):               #打印
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1  #任务倒计时-1
            if self.timeRemaining <= 0:
                self.currentTask = None  #打印完了变空闲
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask = newtask

        self.timeRemaining = newtask.getPages()*60/self.pagerate
                                     #速度是页/min，计算打印秒数
class Task:
    def __init__(self,time):
        self.timestamp = time  #生成时间戳（开始时间）
        self.pages = random.randrange(1,21)  #随机生成打印页数
    def getStamp(self):
        return self.timestamp  #获得任务开始时间戳
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):  #等待时间
        return currenttime - self.timestamp

    
def newPrintTask():  #是否有新作业生成，1/180的概率生成作业
    num = random.randrange(1,181)
    if num == 180: 
        return True
    else:
        return False


def simulation(numSeconds,pagesPerMinute):  #模拟（打印时间，打印速度）
    labprinter = Printer(pagesPerMinute)  #创建一个打印机，并把速度传入
    printQueue = Queue()  #创建一个打印队列，放任务的
    waitingtimes = []     #等待时间列表
    for currentSecond in range(numSeconds):
        if newPrintTask():   #如果有1/180的概率生成的作业
            task = Task(currentSecond)  #创建一个打印任务，并把开始时间传入
            printQueue.enqueue(task)    #把任务放入打印队列
        if (not labprinter.busy()) and (not printQueue.isEmpty()): #不忙且有任务
            nexttask = printQueue.dequeue() #取出打印队列队首的元素
            waitingtimes.append(nexttask.waitTime(currentSecond))
            #把现在时间传入，减去刚刚创建该任务的时间返回等待时间放入等待时间列表
            labprinter.startNext(nexttask)  #把取出元素放入打印机
        labprinter.tick()  #打印任务
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait {:6.2f} secs {:3d} tasks remaing.".\   #平均打印时间和剩余未打印任务
                      format(averageWait,printQueue.size()))

for i in range(10):
    simulation(3600,5)   #打印3600s，打印速度为5页/min
for k in range(10):
    simulation(3600,10)
