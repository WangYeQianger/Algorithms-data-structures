#链表的实现：
#节点Node     #可以理解为节点是地址，节点.getData是所存数据
class Node:
    def __init__(self,initdata):
        self.data = initdata    #initdata 为节点信息
        self.next = None        #地址为空

    def getDate(self):          #获取当前节点数据
        return self.data

    def getNext(self):          #下一节点地址
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
        
#有序表
class OrderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None   #第一个节点是否指向空


    def size(self):
        current = self.head      #指向表头地址
        count = 0
        while current != None:   #地址不为空
            count = count+1
            current = current.getNext()  #指向下一节点地址
        return conut


    def remove(self,item):      #删除是指跳过该节点数据，不是广义上的删除
        current = self.head     #只是将其从单链表内舍去
        previous = None
        found = False
        while not found:
            if current.getDate() == item:
                found = True
            else:
                previous = current   #交错下顺
                current = current.getNext()
        if previous == None:                #如果要删除第一个
            self.head = current.getNext()   #让表头指向当前的下一个即可
        else:
            previous.setNext(current.getNext()) #让前一个数据指向后一个数据


    def search(self,item):
        current = self.head
        found = False
        stop  = False       #有序，引入stop，分区域
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop == True    #后面不会在有所查找的数据，该停了
                else:
                    current = current.getNext()
        return found


    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:  #找到插入位置
            if current.getData() > item:     #在current的前面插入
                stop = True    #后面不会有所查找数据，该停了
            else:
                previous = current
                current = current.getNext()  #交错下顺
                
        temp = Node(item)  #给所插入对象item创建一个节点
        if previous == None:   #如果要在第一个位置插入
            temp.setNext(self.head)  #temp下一节点指向表头所指向的数据
            self.head = temp   #表头指向temp当前节点
        else:                  #插入表中
            temp.setNext(current)    #temp下一节点指向已找到的位置
            previous.setNext(temp)   #previous下一节点指向temp
