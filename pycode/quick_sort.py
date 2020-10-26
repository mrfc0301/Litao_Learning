# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月10日
"""
#快速排序
def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

#归位
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

li = [2,5,8,6,9,3,1,4,7]
quick_sort(li, 0, len(li) - 1)
print(li)