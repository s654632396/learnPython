# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

# 建立 python 和MySQL的连接对象 connenction

import pymysql

ship_list = [
    ('金刚', 1000000001),
    ('小天使', 1000000002),
    ('时雨', 1000000003),
    ('夕立', 1000000004),
    ('俾斯麦', 1000000005),
    ('Abukuma', 1000000006),
    ('北上', 1000000007),
    ('大井', 1000000008),
    ('雷', 1000000009),
    ('熊野', 1000000010),
]

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
    # @todo
    # sql = 'CREATE TABLE `kantai` (' \
    #       '`id` INT(10) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
    #       '`ship_name` VARCHAR(100) NULL,' \
    #       '`ship_id` INT(10) NOT NULL UNIQUE' \
    #       ') ENGINE=INNODB;'
    # sql = 'INSERT INTO `kantai` (`ship_name`,`ship_id`) VALUES '
    # for index,ship in enumerate(ship_list):
    #     sql += '("' + ship[0] + '", ' + str(ship[1]) + ')'
    #     if index + 1 == len(ship_list):
    #         sql += ';'
    #     else:
    #         sql += ',\n'
    sql = "SELECT * FROM `kantai`;"
    cursor.execute(sql)
    print cursor.rowcount

    rs = cursor.fetchone()
    print rs
    rs = cursor.fetchmany(3)
    print rs
    rs = cursor.fetchall()
    print rs

except Exception, e:
    # 回滚
    print e
    connection.rollback()
# 提交事务
connection.commit()

cursor.close()
connection.close()
