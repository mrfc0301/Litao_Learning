# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月31日
"""
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

# 数字拼接问题
def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return ''.join(li)

print(number_join(li))