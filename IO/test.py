# coding=utf-8

# f = open('./test','a')
# f.write('print "write test"')
# f.close()

# f = open('test', 'r+')
# f.write('test r+')
# f.close()

# f = open('test')
# print f.readline().strip()
# print f.readline().strip()
# print f.readline().strip()
# print f.readline().strip()
# f.close()

# import io
# print io.DEFAULT_BUFFER_SIZE
# f = open('test')
# print len(f.readlines(1))
# print len(f.readlines(1))
# print len(f.readlines(1))
# print len(f.readlines(1))
# print len(f.readlines(1))
# print len(f.readlines(1))
# f.close()

# 推荐使用迭代器的方式来操作文件
# f = open('test')
# iter_f = iter(f)
# lineNum = 0
# for line in iter_f:
#     lineNum += 1
# f.close()
# print lineNum
