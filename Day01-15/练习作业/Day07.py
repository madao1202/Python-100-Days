#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/22 22:27
# @Name    : Day07.py
# @Author  : 风暴降生郭德纲
import sys
def Fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        yield x

n= int(input('请输入一个正整数：'))
num = (list(Fibonacci(n)))
print(sys.getsizeof(num))

items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)

import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        #os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()