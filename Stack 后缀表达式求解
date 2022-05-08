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
        
        
        
#后缀表达式求解
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:                   #不是操作数就把栈顶两个元素拿出来进行计算
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)   #把计算结果放入栈顶
    return operandStack.pop()           #最后一个元素就是最终结果
def doMath(op,op1,op2):
    if op == "*":
        return op1 * op2
    if op == "/":
        return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2
