# -*- coding:utf-8 -*-

# python 自带的int() 函数，有2个参数， 第二个参数是转换进制
print int('123')
print int('123', 8)

def pow_number(num, m = 2) :
    re = 1
    while m > 0 :
        re *= num
        m -= 1

    return re

print pow_number(5)

def greet(name = 'world') :
    print 'hello,' + name

greet('haruharu')
greet()

# python 的可变参数
def fn(*args) :
    print args

fn()
fn('a')
fn('a', 'b')
fn('a', 'b', 'c')

def average(*args) :
    sum = 0.0
    if len(args) == 0 : return 0
    for num in args :
        sum += num
    return sum / len(args)

print average(1, 3, 5, 7, 9)