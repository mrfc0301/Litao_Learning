# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年11月02日
"""
# 分数表示
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def gbs(self, a, b):
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fm = self.gbs(b, d)
        fz = a * fm / b + c * fm / d
        return Fraction(fz, fm)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)