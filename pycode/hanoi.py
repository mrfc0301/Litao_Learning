# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月09日
"""
#汉诺塔问题
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')