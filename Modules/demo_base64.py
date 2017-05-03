# coding=utf-8

"""
base64的原理
1. 准备号一个包含了 64 个字符的数组A
2. 对binary data进行处理，每 3byte 为一个组(3*8=24bit)，划4部分，每部分就是6个bit
3. 每个部分，就是 0-63 (2^6=64)的数字，对应数组A的64个元素
4. 然后乡音获取对应的4部分的字符，就是编码后的字符串
5. 所以，Base64编码会把3byte的binary data 转化为 4byte的文本数据，长度plus33%
6. 如果要encode的binary data不是3的倍数，那么剩下的1~2个，Base64会用\x00字节在末尾补足后
7. 再在编码的末尾加上1~2个 = 
8. 这样解码的时候，就可以自动去掉
"""


import base64

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluZw==')

"""
由于标准base64编码后，可能会出现字符+ 和 /
在url中不能直接作为参数传递，所以又有一种 url safe 的base64
就是把 + 和 / ，变成了：
- 和 _
"""
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')

"""
因为 = 字符也可能出现在base64中，但是在url和cookie中可能会造成歧义，所以很多Base64会把末尾的=去掉
因为 base64编码永远是4的倍数，所以
解码的时候，会自动补齐=，然后在进行正常的解码
"""
