# -*- coding:utf-8 -*-

# 使用os模块打开文件

# os.open(fname, flag[, mode])
# flag : 打开文件方式
# os.O_CREAT 只创建文件
# os.O_RDONLY 只读方式打开
# os.O_WRONLY 只写方式打开
# os.O_RDWR  读写方式打开

# os.read(fd, filesize)
# os.write(fd, string)
# os.lseek(fd, pos, how)
# os.close(fd)

import os
# fd = os.open('test2', os.O_CREAT | os.O_WRONLY)
# os.write(fd, '这是一个os创建的文件')
# os.close(fd)

# os module中其他的常用方法
# access(path, mode) 判断权限
# print os.access('test2', os.F_OK)
# print os.access('test2', os.R_OK)
# print os.access('test2', os.W_OK)
# print os.access('test2', os.X_OK)
#
# print os.access('test3', os.F_OK)

# listdir(path) 返回指定目录下，所有文件组成的列表
# print os.listdir('../')

# rename(old_name, new_name) 修改名字
# print os.listdir('./')
# print os.rename('test2', 'test3')
# print os.listdir('./')

# remove(path) 删除操作
# print os.listdir('./')
# os.remove('test3')
# print os.listdir('./')

# mkdir(path[, mode]) 创建一个目录
# makedirs(path[, mode]) 创建多级目录
# removedirs(path) 删除多级目录
# rmdir(path) 删除空目录

# os.makedirs('testdir/test/ttt')

# os.path module的常用方法
# exists(path) 判断当前路径是否存在
# isdir(s) 判断路径是否是一个目录
# isfile(path) 判断路径是否是一个文件
# getsize(filename) 获取文件的大小
# dirname(path) 返回路径的目录
# basename(path) 返回路径的文件名

print os.path.exists('test')
print os.path.exists('test2')
print os.path.isdir('test')
print os.path.isfile('test')
print os.path.getsize('test')

print os.path.dirname('/home/haruharu/pys/IO/test')
print os.path.basename('/home/haruharu/pys/IO/test')






























