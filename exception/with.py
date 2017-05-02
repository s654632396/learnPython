# coding=utf-8

# with content [as var[:
# with_suite

# with语句用来代替try except finally语句， 使代码更简洁
# context 表达式返回一个对象
# var 用来保存context返回的对象， 单个返回值/元祖
# with_suite 使用var标量来对context对象进行操作

# with open('1.txt') as f :
#     for line in f.readlines():
#         print line

# 1. open 1.txt
# 2. f 变量接收了对象返回的对象
# 3, with中的代码执行完毕后，关闭文件

class Mycontext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print '__enter__'
        return self

    def doSomething(self):
        print 'doing some thing ..'
        a

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != None :
            print "Error[", exc_type, "] info :", exc_val
        print '__exit__'

with Mycontext('test') as f:
    print f.name
    f.doSomething()

# with context 对象，由__enter__ 方法返回value，由as语句接收
# 执行完或者执行中发生异常，会执行__exit__，然后再将异常交给外部(上级)处理
