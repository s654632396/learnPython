# coding=utf-8

# 标准异常： Built-In Exceptions
# BaseException
#      |                |               |
# KeyboardInterrupt   Exception     SystemExit
#                       |
#              SyntaxError, NameError, ValueError...

# 自定义异常
# 描述python没有涉及的异常
# 必须继承 Exception
# 自定义异常只能主动抛出

class FileError(IOError):
    pass
try:
    raise FileError, "test FileError"
except FileError, e:
    print e

