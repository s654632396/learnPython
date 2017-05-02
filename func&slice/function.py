# -*- coding:utf-8 -*-

# https://docs.python.org/2/library/functions.html

# 调用函数的时候，如果传入的参数不对，则会报TypeError错误

if False :
    # 比较函数 cmp(x, y) 如果 x < y return -1, x == y return 0, x > y return 1

    print cmp(12, 14)
    print cmp(12, 12)
    print cmp(-10, -12)

    # int() 函数将其他数据类型转换成 int
    print int('123') # 123
    print int(True) # 123
    print int(False) # 123

    #print int('123aaa') # ValueError: invalid literal for int() with base 10: '123aaa'

    # str() 将其他类型转换成 string
    print str(12312321)
    print str(-100)
    print str(False)

lis = []
n = 1
while n <= 100 :
    lis.append(n * n)
    n += 1
print sum(lis)