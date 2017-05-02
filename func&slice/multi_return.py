# -*- coding:utf-8 -*-

# 在python函数中，返回多个值

# math包提供了sin() 和 cos() 函数
import math

def move(x, y, step, angle) :
    nx = x + step + math.cos(angle)
    ny = y + step + math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

# 实际上， python是返回的一个tuple
r = move(100, 100, 60, math.pi / 6)
print r

# 一元二次方程 ax^2 + bx + c = 0
def my_equation(a, b, c) :
    # 参考求根公式 x = (-b ± gen(b^2 - 4ac)) / 2a
    t =  math.sqrt(math.pow(b, 2) - 4 * a * c)
    return (-b + t) / (2 * a),(-b - t) / (2 * a)

print my_equation(2, 3, 0)
print my_equation(1, -6, 5)