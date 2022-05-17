#递归实现：整数转换为任意进制
def toStr(n,base):   # n为所需转换数字，base为所转换进制（进制基）
    convertString = "0123456789ABCDEF"   #所查表
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]

#eg:  3 →2进制   走else返回 3//2=1进入函数，找到 '1' + '1' =3%2
#eg:  10→2进制   //:5  2  1  0
#                 %:0  1  0  1      把0101反着输出1010
#
#eg:  17→2进制   //:8  4  2  1  0
#                 %:1  0  0  0  1   10001 反着 10001
#
#eg:  19→2进制   //:9  4  2  1  0
#                   1  1  0  0  1   11001 反着 10011


print(toStr(255,2))
print(toStr(10,2))
print(toStr(17,2))
print(toStr(19,2))

import sys
sys.getrecursionlimit()      #获取最大递归深度
sys.setrecursionlimit(2000)  #调整最大递归深度
