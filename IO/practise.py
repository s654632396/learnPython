# -*- coding:utf-8 -*-

import ConfigParser
cp = ConfigParser.ConfigParser()
# print cp
cp.read('test.ini') # 读取配置文件
# print cp.sections()
for sec in cp.sections():
    print sec
    print cp.items(sec)

# set(section, key, new_value)
cp.set('userinfo', 'pwd', '12345678')
cp.remove_option('skill', 'linux')
# cp.remove_section('skill')

# for sec in cp.sections():
#     print sec
#     print cp.items(sec)

# 保存的步骤
fp = open('test.ini', 'w')
cp.write(fp)
fp.close()