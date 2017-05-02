# coding=utf-8

# 取2个数的最大公约数(欧几里德算法)
# gcd(a, b) = gcd(b, a mod b)
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def gcd_while(a, b):
    if (a < b):
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

# stein算法-
def gcd_stein(a, b) :
    pass
# 有理数 Rational 类
# p q 都是整数，表示有理数 p/q
# 如果想要Rational进行 + 运算，则实现 __add__() 方法
class Rational(object):
    def __init__(self, p, q):
        self.p = p  # 分子
        self.q = q  # 分母

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - r.q * self.q, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    __repr__ = __str__

if __name__ == '__main__':
    r1 = Rational(1, 3)
    r2 = Rational(1, 2)
    print r1 + r2
    print r1 - r2
    print r1 * r2
    print r1 / r2
