# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月20日
"""
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

def creat_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def creat_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(li):
    while li:
        print(li.item, end=',')
        li = li.next

# li = creat_linklist_head([1,2,3])
# print_linklist(li)
lk = creat_linklist_tail([1,2,3])
print_linklist(lk)
