# -*- coding:utf-8 -*-
"""
作者：李涛
日期：2020年10月09日
"""
import time

#测量函数运行时间
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper