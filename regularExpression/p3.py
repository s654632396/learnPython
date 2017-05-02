# coding=utf-8 

import re

string = 'this number is 1000 and next is 200'

# print string.find('200')
num = re.search(r'\d+', string)
print num.group()

string2 = 'c++=100, php=800, python=1000,java=400'
nums = re.findall(r'\d+', string2)
print nums
# print sum([int(x) for x in nums])

# sub(pattern, repl, string, count=0, flags=0)
# 将string中匹配到的部分，替换为其他值

string3 = 'c++=100, php=800, python=1000,java=400'


def add_one(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


info = re.sub(r'\d+', add_one, string3)
print string3
print info

# split(pattern, string, maxsplit=0, flags=0)
# 根据匹配分割字符串，返回分割字符串组成的列表
string4 = 'heqiang:C,C#,PHP,Python MySQL HTML;dongchaofeng:C,C++,Java,PHP,Python MySQL ???'
print re.split(r':| |,|;', string4, 0)
