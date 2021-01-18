
# 1、函数的定义和调用
# 定义函数
def add_num(a, b):
    result = a + b
    print(result)
# 调用函数
add_num(10, 20)
# 2、函数的返回值
# 2.1 例
# 定义函数
def buy():
    return '烟'
# 调用函数
# 接收函数返回值
good = buy()
print(good)
# 2.2 练习
# 需求：制作⼀个计算器器，计算任意两数字之和，并保存结果。
# 定义函数
def num(a, b):
    # 函数说明文档
    """ 求和函数"""
    return a + b
#键盘接收到的数据类型为字符串这里需要做运算应为数值型，所以需要进行强制类型转换
num1 = int(input('请输入数字1：'))
num2 = int(input('请输入数字2：'))
# 接收返回值
result = num(num1, num2)
print(result)
help(num)



