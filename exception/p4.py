# coding=utf-8

# try except finally
# 1. try 没有捕捉到异常，执行完 try 后，执行finally
# 2. try 捕捉到了异常，先执行 except 处理错误， 再执行 finally

try:
    f = open('1.txt')
    line = f.read(2)
    num = int(line)
    print 'read num = %d' % num
except IOError, e:
    print 'catch IOerror: ', e
except ValueError, e:
    print 'catch ValueError: ', e
else:
    print 'No Error..'

finally:
    try :
        f.close()
    except NameError, e:
        print 'catch NameError:', e
    print 'close file ..'

# try except else finally



