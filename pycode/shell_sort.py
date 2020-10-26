# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月11日
"""
#按步长进行插入排序
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp
#希尔排序
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

li = list(range(100))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)