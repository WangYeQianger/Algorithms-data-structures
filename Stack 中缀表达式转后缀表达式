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
        
        
        
#将中缀表达式转变为后缀表达式
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []      #储存单词
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token) #把单词加到列表里
        elif token == '(':
            opStack.push(token)       #把括号加到栈里
        elif token == ')':
            topToken = opStack.pop()  #将栈顶元素取出
            while topToken !='(':     #只要栈顶元素不是左括号就把它放入列表
                postfixList.append(topToken)
                topToken = opStack.pop()   #栈里最后一个左括号呗topToken 吃了
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>= prec[token]):
                postfixList.append(opStack.pop())  #不空且栈顶优先级比当前大,把栈顶元素放入列表
            opStack.push(token)   #结束后把当前元素放入栈顶
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())  #把栈顶元素一一取出放入列表
    return " ".join(postfixList)


    ##  eg : A+B*C+D → ABC*+D   (A+B)*C+D → AB+C*D+
    ##  列表  [ A B C * + D 
    ##    栈  [ + (*) (+)(判断 * > + 把*放入列表,+ = +,把 + 放入列表)   栈非空，一一放入
    ##  如果单词是左括号 （ 压入栈顶
    ##  如果单词是右括号  ）则反复弹出栈顶操作符加到列表，直到碰到左括号
    ##  列表  [ A B + C * D +
    ##    栈  [ ( (+) (*) + (碰到右括号只要栈顶元素不是左括号就往列表里放 优先运算）
