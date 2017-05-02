# -*- coding:utf-8 -*-

def f1(x):
    pass


print f1.__name__  # f1


def log(f):
    def wrapper(*args, **kw):
        print 'call ...'
        return f(*args, **kw)

    return wrapper


@log
def f2(x):
    pass


print f2.__name__  # wrapper


def log(f):
    def wrapper(*args, **kw):
        print 'call ...'
        return f(*args, **kw)

    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper


@log
def f3(x):
    pass


print f3.__name__  # f3

# 为了减少复制操作，python内置了 functools 可以自动完成copy的任务
import functools


def log(f):
    @functools.wraps(f)
    def wrapper(*args, **ke):
        print 'call ...'
        return f(*args, **ke)

    return wrapper

def f4(x) :
        pass
print f4.__name__ # f4


sorted_ignore_case = functools.partial(sorted, cmp = lambda x, y : cmp(x.upper(), y.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])



































