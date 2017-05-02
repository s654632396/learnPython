# -*- coding:utf-8 -*-

# 建立 python 和MySQL的连接对象 connenction

import pymysql

connection = pymysql.Connect(host='127.0.0.1',
                             user='appdev',
                             password='123456',
                             port=3316,
                             db='pythondb',
                             charset='utf8')
# 开始事务处理
connection.begin()
try :
    # 使用该连接创建并返回游标
    cursor = connection.cursor()


    print connection
    print cursor
except Exception, e:
    # 回滚
    connection.rollback()
# 提交事务
connection.commit()

cursor.close()
connection.close()





























