# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月09日
"""
#简单的选择排序
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

#选择排序
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[min_loc], li[i] = li[i], li[min_loc]
        print(li)

li = [2,5,8,6,9,3,1,4,7]
#print(select_sort_simple(li))
print(li)
select_sort(li)