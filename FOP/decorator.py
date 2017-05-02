# -*- coding:utf-8 -*-

# 装饰器

# decorator 本质上就是一个高阶函数
# 它接受一个函数作为参数，然后返回一个新的函数

# 使用 @ 语法，这样可以避免手写  f = decorate(f) 这样的代码
# 使 @log 自适应任何参数定义的函数，可以利用 *args 和 **kw
# 保证任意个数的参数总是可以正常调用

def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()..'
        return f(*args, **kw)

    return fn


import time
def perfomance(perfix):
    def per_perfomance(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if perfix == 'ms' :
                t = (t2 - t1) * 1000
            else :
                t = t2 - t1
            print 'call %s() in %f%s' % (f.__name__, t, perfix)
            return r
        return fn
    return per_perfomance

@perfomance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)

# print log(abs)(-10)
# print log(cmp)(100, 200)
