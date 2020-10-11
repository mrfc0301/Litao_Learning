# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月09日
"""
from cal_time import *

@cal_time
#顺序查找
def linear_search(li,val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return None

@cal_time
#二分查找
def bianry_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None

li = list(range(100000))

linear_search(li,38900)
bianry_search(li,38900)