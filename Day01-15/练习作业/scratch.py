import sys
# list1 = [1, 25, 7, 34, 200]
# list1.append(15)
# b='你好'
# c=198%10
# list1+=['汉字', b, c]
# list2 = list1.copy()
# list2.insert(3, 25)
# print(list1)
# print(list2)
# list3 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list4 = sorted(list3)
# print(list4)
# for x in range(1,10):
#     for y in range(1,x+1):
#         print('%d*%d=%d'%(x,y,x*y),end='\t')
#     print()
# list5 = []
# star = '*'
# line = '_'
# for i in range(1,6):
#     print((star + line + star+' ')*i)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# print(' '.join(f))
# for x in 'ABCDE':
#     for y in [1,2,3,4,5,6,7]:
#         print(f'{x}{y}',end='\t')
#     print()
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f)) # 查看对象占用内存的字节数
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f)) # 相比生成式生成器不占用存储数据的空间
# content = '北京欢迎你为你开天辟地…………'
# print(content[1:])
# print(content[0])
# print(content[1:]+content[0])
# all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(len(all_chars) - 1)
import string
import random


def generate_random_code(n=4):
    all_chars = string.digits + string.ascii_letters
    return ''.join(random.choices(all_chars, k = n))


# 示例用法
code_length = 10
random_code = generate_random_code()
print(random_code)
