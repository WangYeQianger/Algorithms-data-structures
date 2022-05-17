class Stack:
    def __init__(self):
        self.items = []          # .items 查看栈的内容

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
        
        
#将任意十进制数转换成 16以下任意base进制
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber>0:
        rem = decNumber % base         #除base 取余数 倒着输出
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]  #不断从栈顶取出

    return newString
