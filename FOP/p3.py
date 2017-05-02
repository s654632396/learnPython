# -*- coding:utf-8 -*-

def f(x):
    return x * x


print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def format_uname(name):
    if isinstance(name, str):
        return name[0].upper() + name[1:].lower()
    return


names = ['admin', 'LISA', 'barT']
print map(format_uname, names)


def f(x, y):
    return x + y


print reduce(f, range(1, 11), 100)

def c(x, y):
    return x * y

print reduce(c, range(1, 11))
