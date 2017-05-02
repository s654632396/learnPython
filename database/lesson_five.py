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
    shipname, shipid = '晓', 1000000014
    cursor = connection.cursor()
    # sql_insert = "INSERT INTO `kantai` (`ship_name`,`ship_id`) VALUES " \
    #              "('%s', %d);" % (shipname, shipid)
    # cursor.execute(sql_insert)
    # bargs = {'shipname2': '咖喱', 'shipid2': 1000000013, '_id': 40}
    # sql_update = "UPDATE `kantai` SET `ship_name`=%(shipname2)s,`ship_id`=%(shipid2)s WHERE `id`=%(_id)s;"
    # cursor.execute(sql_update, bargs)
    # args = ['响爷', 1000000015, 40]
    # sql_update = "UPDATE `kantai` SET `ship_name`=%s,`ship_id`=%s WHERE `id`=%s;"
    # cursor.execute(sql_update, args)


except Exception, e:
    # 回滚
    print e
    connection.rollback()
# 提交事务
connection.commit()

cursor.close()
connection.close()
