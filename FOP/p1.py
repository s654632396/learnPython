# -*- coding:utf-8 -*-

# 函数式编程

# 变量可以指向函数

print abs(-10)

f = abs
print f # <built-in function abs>
print f(-10)

# 函数名其实就是指向函数的变量
abs = len
print abs([1, 2, 3])

# 高阶函数：能够接受函数做参数的函数
## 变量可以指向函数
## 函数的参数可以接受变量
### 一个函数可以接受另一个函数作为参数
# 这就是高阶函数


