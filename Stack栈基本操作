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


s = Stack()

print(s.isEmpty())
s.push(4)
s.push('沐晨汐啊')
print(s.peek())        #窥视栈顶元素
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(3.1415926)
print(s.pop())
print(s.pop())
print(s.size())
