# -*- coding:utf-8 -*-

# python 常见错误
# 1. NameError
# 2. SyntaxError
# 3. IOError
# 4. 10/0 => ZeroDivisionError
# 5. ValueError
# 6. KeyboardInterrupt

# try -- except 异常处理
# try :
#     try_suite
# except Exception [e]:
#     exception_block

# a = 12
try:
    # a
    pass
except NameError, e:
    print 'catch error:', e

# print 'exe over'

# try except 是捕获处理 运行时的错误，不能截获语法错误这类型的运行前错误

# 处理多个异常
try:
    f = open('1.txt')
    line = f.read(2)
    num = int(line)
    print 'read num=%d' % num
except IOError, e:
    print 'catch error:', e
except ValueError, e:
    print 'catch valueError:', e
