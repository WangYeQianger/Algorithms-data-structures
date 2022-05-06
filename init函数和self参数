##class Rectangle():
##    def getPeri(self,a,b):
##        return (a + b)*2
##    def getArea(self,a,b):
##        return a*b
##
##rect = Rectangle()
##print(rect.getPeri(3,4))
##print(rect.getArea(3,4))
##print(rect.__dict__)

class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getPeri(self):
        return (self.a + self.b)*2
    def getArea(self):
        return self.a * self.b

rect = Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())
print(rect.__dict__)

##从上面的结果可以看到定义完init()后
##创建的每个实例都有自己的属性，可以直接调用类中的函数。



class Person:

    def print_info(self):
        if str.lower(self.gender)=='female':
            print('Her name is {}, she is {} years old'.format(self.name,self.age))
        elif str.lower(self.gender)=='male':
            print('His name is {}, he is {} years old'.format(self.name,self.age))
        else:
            print('ERROR')

            
##    #方法一
##    def __init__(self):
##        self.name=None
##        self.gender=None
##        self.age=None
##
##person = Person()   
##person.name='lisa'
##person.gender='female'
##person.age=18
##person.print_info()

            
    #方法二
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

person2=Person('lisi','male',20)
person2.print_info()


##主要的区别在于：
##前者定义类可以是一个空结构，当有输入进来的时候再添加相应的数据；
##后者则必须传值，不予许为空值。
