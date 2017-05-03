# coding=utf-8

"""
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
"""

import threading, time

balance = 0


def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_proc(n):
    for i in range(100000):
        change_balance(n)


if __name__ == '__main__':
    t1 = threading.Thread(target=run_proc, name='task_1', args=[5, ])
    t2 = threading.Thread(target=run_proc, name='task_2', args=[8, ])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'balance=%s' % balance

"""
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
也分两步：
计算balance + n，存入临时变量中；
将临时变量的值赋给balance

两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，
所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。


"""