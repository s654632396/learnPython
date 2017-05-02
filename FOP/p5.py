# -*- coding:utf-8 -*-

# closure
def count():
    fs = []
    for i in range(1, 4):
        def g(j):
            def f():
                return j * j

            return f

        r = g(i)
        fs.append(r)

    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()

print map(lambda x: x * x, range(1, 10))

# 这里的 lambda x: x * x 等价于
# def f(x) : return x * x

# 关键字 lambda 表示匿名函数 冒号前的x表示函数参数
# 匿名函数有个限制， 就是只能有一个表达式， 不写return
# 返回值就是该表达式的结果

print sorted([1, 45, 5, 75, 33, 12], lambda x, y: -cmp(x, y))

myabs = lambda x : -x if x < 0 else x
print myabs(-199)
print myabs(199)


print filter(lambda x: x and len(x.strip()) > 0, ['test', '', 'str', None, 'END', '   '])































