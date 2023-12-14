# --*-- conding:utf-8 --*--
# @Time : 2023/12/14 23:52
# @Author : 风暴降生郭德纲
# @File : Day04.py
# 练习
# 练习1：输入一个正整数判断是不是素数。
# 提示：素数指的是只能被1和自身整除的大于1的整数。
from math import sqrt

num = int(input('请输入一个正整数：'))
if num>1 and all(num % i for i in range(2, int(sqrt(num)) + 1)):#all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。元素除了是 0、空、None、False 外都算 True。
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
