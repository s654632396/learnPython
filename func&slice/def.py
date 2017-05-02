# -*- coding:utf-8 -*-

def my_abs(x) :
    if x >= 0 :
        return x
    else :
        return -x

# return None 可以写作 return


print my_abs(-100)
print my_abs(500)

def square_of_sum(_list) :
    sum = 0.0
    for x in _list :
        sum += x * x
    return sum

