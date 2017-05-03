# coding=utf-8

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run process %s pid of (%d), main pid is %d' % (name, os.getpid(), os.getppid())
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print 'done process %s pid of (%d) execute %2f s' % (name, os.getpid(), end - start)


if __name__ == '__main__':
    print 'main process (%d) run ..' % os.getpid()
    """对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
    ，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
                            p = Pool(5)
    就可以同时跑5个进程
    """
    p = Pool()
    """由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
    """
    for i in range(1, 7):
        p.apply_async(func=long_time_task, args=['task_'+str(i),])

    print 'waiting for all subprocessing done.'
    p.close()
    p.join()

    print 'process end.'