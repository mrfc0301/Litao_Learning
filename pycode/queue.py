# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月18日
"""
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

queue = Queue(5)
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.is_empty())
queue.push(4)
queue.push(5)
print(queue.is_filled())

#内置模块
from collections import deque

queue = deque()
queue.append(1)
queue.appendleft(2)
#print(queue.pop())
print(queue.popleft())