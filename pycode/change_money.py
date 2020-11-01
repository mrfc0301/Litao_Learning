# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月26日
"""
t = [100, 50, 20, 10, 5, 1]

def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

print(change(t, 376))