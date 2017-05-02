# -*- coding:utf-8 -*-

def fact(n) :
    if n == 1:
        return n
    else :
        return n * fact(n - 1)

print fact(3)
print fact(5)
print fact(100)

# 使用递归，要注意防止栈溢出
# 计算机中，函数的调用是通过栈(stack)这种数据结构实现的
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数return，栈就回减少一层栈帧
# 栈的大小并非无限制，所以递归调用次数过多，会导致栈溢出

# print fact(10000)   # RuntimeError: maximum recursion depth exceeded

def hannota(n, a, b, c) :
    if n == 1:
        print a, '-->' , c
        return
    hannota(n -1 , a, c, b)
    print a, '-->', c
    hannota(n -1, b, a, c)

hannota(4, 'A', 'B', 'C')