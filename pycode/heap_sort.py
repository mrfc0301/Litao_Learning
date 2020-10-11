# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月10日
"""
#向下调整
def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    """
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            return
    li[i] = tmp

#topk问题
def topk(li, k):
    heap = li[0:k]
    #建堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    #遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    #输出
    for i in range(k-1, -1, -1):
        heap[0],heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap

import random
li = list(range(100))
random.shuffle(li)
print(topk(li, 10))

#堆排序
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)

# li = [i for i in range(100)]
# import random
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)

# #内置模块
# import heapq
# import random
# li = list(range(100))
# random.shuffle(li)
# print(li)
# heapq.heapify(li) #建堆
# for i in range(len(li)):
#     print(heapq.heappop(li), end=', ')