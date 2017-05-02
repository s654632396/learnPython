# coding=utf-8 

import re

#
# m = re.match(r'[\s\S]*?(\<[a-zA-Z0-9_]+\>).*?', 'this is a \n <String_1>, <maybe> something wrong')
# if m:
#     print m.group(),m.span()
#     print m.groups()
#
# else:
#     print None
#
# m = re.match(r'abc|d', 'abc')
# print m.group()
#
# m = re.match(r'(([\w]{1,16})@(163|126)\.com$)', '6h2cdd_7h55@163.com')
# if m:
#     print m.group()
#     print m.groups()
# else:
#     print None
#
# m = re.match(r'<(\w+)>(\w+)?</\1>', '<book>123</book>')
# print m.group()
# print m.groups()

m = re.match(r'<(?P<mark>\w+?>)(\S+)?</(?P=mark)', '<book>这是一个xml</book>')
print m.group()
for index, ele in enumerate(m.groups()):
    print 'ele' + str(index) + ' :', ele.decode('utf-8')
