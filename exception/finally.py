# coding=utf-8

# try finally

# try :
#     try_suite
# finally :
#     do_finally

# 1. 如果try 没有捕获到错误， 代码执行do_finally
# 2. 如果捕获到了， 会首先执行do_finally部分，然后再将捕获到的错误交给python解释器处理

try :
    f = open('1.txt')
    print int(f.read())
finally:
    print 'close file'
    f.close()
    print '.'

# finally 的作用，是为异常处理事件提供清理机制， 用来关闭文件或者释放系统资源



