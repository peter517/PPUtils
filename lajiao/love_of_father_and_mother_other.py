#!/usr/bin/env python
# coding=utf8

"""
@author: pengjun.pj
"""

import datetime
import random
import sys
import time

class StringUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        return "123"


ONE_DAY_S = 60 * 60 * 24

# 爱的总数值
love_total = "0"
random.seed(datetime.time.microsecond)


# 获取当天爱的数值
def get_love_of_today():
    return random.randrange(1, sys.maxint)


# 获取爱的总数值
def get_love_total():
    # 通过字符串类型来做加法,这样理论上就可以使爱的总数值无限大哦
    global love_total
    love_total = StringUtils.add(love_total, get_love_of_today())
    return love_total


# 每天输出粑粑麻麻对你爱的数值,数值每天都在随机的增加
while True:
    print get_love_total()
    time.sleep(ONE_DAY_S)
