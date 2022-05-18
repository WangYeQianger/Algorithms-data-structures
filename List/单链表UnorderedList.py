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
        
       
#无序表
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):             #复杂度为 O(1)
        return self.head == None   #第一个节点是否指向空


    def add(self,item):          #大概意思就是，[1]里加个temp→[temp,1],先创一个节点temp，然后把表头所指向的1放到它的下一个节点上，然后再把表头指向temp.
        temp = Node(item)        #设定一个节点，存放数据为item
        temp.setNext(self.head)  #temp下一个节点指向表头所指节点的数据
        self.head = temp         #表头指向 temp

        
    def size(self):
        current = self.head      #指向表头地址
        count = 0
        while current != None:   #地址不为空
            count = count+1
            current = current.getNext()  #指向下一节点地址
        return conut


    def search(self,item):
        current = self.head    #指向表头地址
        found = False
        while current != None and not found:
            if current.getDate() == item:     #获取节点数据
                found = True
            else:
                current = current.getNext()   #指向下节点地址
        return found


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

