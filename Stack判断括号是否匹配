class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
        
#判断括号是否匹配yeh
def match(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)        #如果是左括号就放到栈里
        else:
            if s.isEmpty():   
                balanced = False
            else:                 #不是左括号
                top = s.pop()     #栈顶元素和所遍历到元素匹配
                if not match(top,symbol):  
                    balanced = False
        index +=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
