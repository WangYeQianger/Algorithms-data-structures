#ADT Deque 双端队列实现       队首在list最右端，队尾在最左端
class Deque:
    def __init__(self):
        self.items = []             # .items  查看序列内容

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#判断回文字符串

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)      #把字符串一个个加到队列里
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last  = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

print(palchecker("我是王业强啊强业王是我"))
print(palchecker("abcdefghijklmnopqrstuvwxyz"))
