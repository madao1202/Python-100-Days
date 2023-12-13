# --*-- conding:utf-8 --*--
# @Time : 2023/12/13 1:26
# @Author : 风暴降生郭德纲
# @File : Day02.py
### 练习

#### 练习1：华氏温度转换为摄氏温度。
####提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
Temperature = float(input("华氏温度为："))
Out = (Temperature - 32) * 5 / 9
print('%.1f 华氏温度=%.1d ℃' % (Temperature, Out))
print(f'{Temperature:.1f}华氏度={Out:.1f}℃')
