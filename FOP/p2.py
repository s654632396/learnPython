# -*- coding:utf-8 -*-

# 定义一个函数 ，接受 x y f 3个参数
# 其中 x y 是数值， f是函数

import math

def add(x, y, f) :
    return f(abs(x)) + f(abs(y))

print add(-5, 9, abs)

print add(-5, 9, math.sqrt)