# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月31日
"""
# 钢条切割问题
from cal_time import*

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n-i))
        return res

@cal_time
def c1(p, n):
    return cut_rod_recurision_1(p, n)

def cut_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_rod_recurision_2(p, n-i))
        return res

@cal_time
def c2(p, n):
    return cut_rod_recurision_2(p, n)

@cal_time
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i-j])
        r.append(res)
    return r[n]

print(c1(p, 15))
print(c2(p, 15))
print(cut_rod_dp(p, 15))