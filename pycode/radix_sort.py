# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月11日
"""
#基数排序
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1

import random
li = list(range(10000))
random.shuffle(li)
radix_sort(li)
print(li)