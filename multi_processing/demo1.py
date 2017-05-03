# coding=utf-8

import os

print 'Process (%s) Start!' % os.getpid()

pid = os.fork()

if pid == 0 :
    print 'this is a child process (%s) and my parent is (%s)' % (os.getpid(), os.getppid())
else:
    print 'my process id is (%s) and i\' create process (%s)' % (os.getpid(), pid)

