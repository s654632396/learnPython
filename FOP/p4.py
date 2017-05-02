# -*- coding:utf-8 -*-

# 过滤偶数
def is_odd(x):
    return x % 2 == 1


print filter(is_odd, range(1, 11))


# 去空
def notEmpty(x):
    return x and len(x.strip()) > 0


print filter(notEmpty, ['tets', None, '', 'src', '\t\t123\r\n', 'END'])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


L = [12, 5, 156, 7, 21]
print sorted(L, reversed_cmp, None, True)

def f() :
    print 'call f()'
    def g():
        print 'call g()'
    return g

g = f()   # <function g at 0x7f7ee72a57d0>

#
def calc_prod(lst) :
    def multiply() :
        re = 1
        for val in lst :
            re *= val
        return re
    return multiply

f = calc_prod([1,2,3,4,5])
print f()


