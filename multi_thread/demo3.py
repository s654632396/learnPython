# coding=utf-8

"""
如果我们要确保balance计算正确，就要给change_it()上一把锁，
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现
"""
import threading, time

balance = 0

def run_proc(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_balance(n)
        finally:
            lock.release()

lock = threading.Lock()
def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n

if __name__ == '__main__':
    t1 = threading.Thread(target=run_proc, name='task_1', args=[5, ])
    t2 = threading.Thread(target=run_proc, name='task_2', args=[8, ])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'balance=%s' % balance