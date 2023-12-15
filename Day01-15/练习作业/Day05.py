# --*-- conding:utf-8 --*--
# @Time : 2023/12/16 3:43
# @Author : 风暴降生郭德纲
# @File : Day05.py
# 练习1：水仙花数
# for循环遍历100-999之间的数range（100，1000）；
# 判断是否为水仙花数:（判断条件：百位数的立方+十位数的立方+个位数的立方==这个数)
# x,y,z=i//100,i//10%10,i%10
# if x**3+y**3+z**3==i:true;else:false

num = []
for i in range(100, 1000):
    x, y, z = i // 100, i // 10 % 10, i % 10
    if x ** 3 + y ** 3 + z ** 3 == i:
        num.append(i)
    num.reverse()
print('水仙花有:', end='')
for number in num:
    print(number, end=' ')

# 练习2：正整数的反转
# 从个位数开始加起，每次加完后，原数除以10，再取余数，直到原数为0
print('')  # 换行
num = int(input('请输入一个正整数：'))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10  # 赋值运算符
print(reverse)

# 练习3：给定单价、总价和总数量计算每个商品购买数量
# 1.穷举法：三层循环，枚举公鸡、母鸡、小鸡的所有可能性，再判断是否满足条件
x = float(input('公鸡的价格是'))
y = float(input('母鸡的价格是：'))
z = float(input('小鸡的价格是：'))
price = float(input('总共花了多少钱：'))
quantity = int(input('总共买了多少只：'))
for i in range(0, quantity):
    for j in range(0, quantity - i):
        for k in range(0, quantity - i - j + 1):
            if i + j + k == quantity and x * i + y * j + z * k == price:
                print('买了公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, k))

# 练习4：斐波那契数列 练习赋值和while循环部分
i = 1
j = 1
num = 0
print(1, 1, end=' ')
while num < 30:
    num = i + j
    i = j
    j = num
    print(num, end=' ')

# 练习5：完美数
# 计算10000以内的完美数
for num in range(1, 10000):
    sum = 0
    for factor in range(1, num):  # 因子
        if num % factor == 0:
            sum += factor
    if sum == num:
        print(num, end=' ')
