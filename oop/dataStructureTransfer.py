# coding=utf-8

# 导入新版的除法
from __future__ import division
# 先跳入上级目录
import sys
sys.path.append('..')
# 导入隔壁的math的gcd函数
from oop.math import gcd

# 类型转化
class Rational(object):
    def __init__(self, p, q):
        self.p = p  # 分子
        self.q = q  # 分母

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    __repr__ = __str__

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q

r1 = Rational(12, 4)
print int(r1)
print float(r1)