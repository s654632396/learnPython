# coding=utf-8

"""
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
"""

from multiprocessing import Queue, Process
import os, time


def writeQueue(q):
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        print 'put data [%s] into Queue..' % v
        q.put(v)
        time.sleep(3)


def readQueue(q):
    while True:
        msg = q.get()
        print 'get data [%s] from write.' % msg
        # time.sleep(4)


if __name__ == '__main__':
    # 父进程创建Queue
    q = Queue()
    pw = Process(target=writeQueue, args=[q])
    pr = Process(target=readQueue, args=[q])

    pw.start()  # 写的进程开始写数据

    pr.start()  # read process start


    pw.join()
    pr.terminate()  # 死循环进程，用terminate杀死
    print 'process read done.'
    print 'End process.'

"""Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
父进程所有Python对象都必须通过pickle序列化再传到子进程去，
所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
"""