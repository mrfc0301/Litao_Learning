# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月10日
"""
#插入排序
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

li = [2,5,8,6,9,3,1,4,7]
print(li)
insert_sort(li)