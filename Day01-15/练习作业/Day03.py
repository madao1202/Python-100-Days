# --*-- conding:utf-8 --*--
# @Time : 2023/12/13 20:44
# @Author : 风暴降生郭德纲
# @File : Day03.py
##练习1：英制单位英寸与公制单位厘米互换。
value = input('输入长度：')
try:
    value = float(value)
    Unit = float(input('输入长度单位（1是英寸，2是厘米):'))
    if Unit == 1:
        print('%.f 英寸等于%.f厘米' % (value, value * 2.54))
    elif Unit == 2:
        print('%.f 厘米等于 %.f英寸' % (value, value / 2.54))
    else:
        print('无效输入，请输入1or2')
except ValueError:
    print('长度类型错，请输入数字')
#if value.isnumeric():
#if value.isdigit(): //都不能判断浮点数
    #value = float(value)

#else:
    #print('长度请输入数字')

