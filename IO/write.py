# coding=utf-8

list_f = []

for i in range(1025) :
    list_f.append(open('test2','w'))
    print "%d, %d" % (i, list_f[i].fileno())

# Traceback (most recent call last):
#   File "write.py", line 6, in <module>
# IOError: [Errno 24] Too many open files: 'test2'
