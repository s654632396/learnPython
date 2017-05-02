# coding=utf-8

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
try:
    # 使用该连接创建并返回游标
    cursor = connection.cursor()

    sql = "SELECT * FROM `kantai`;"
    cursor.execute(sql)
    # print cursor.rowcount

    rs = cursor.fetchall()
    for row in rs :
        # print "id=%d,ship_name=%s,ship_id=%d" % (row[0], row[1].encode('utf-8'), row[2])
        print "id=%d,ship_name=%s,ship_id=%d" % (row[0], row[1], row[2])

except Exception, e:
    # 回滚
    print e
    connection.rollback()
# 提交事务
connection.commit()

cursor.close()
connection.close()
