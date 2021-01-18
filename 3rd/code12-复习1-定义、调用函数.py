# 1、定义调用函数
# 定义函数（形参：形式参数）
def add_num(a,b):
    result = a + b
    print(result)
# 调用函数（实参：实际参数）
add_num(20, 20)
add_num(60, 40)
# 需求：制作⼀个计算器，计算任意两数字之和，并保存结果。
# 定义函数
def sum_num(num1, num2):
    # 函数说明文档
    '''求和函数'''
    return num1 + num2
num1 = int(input('请输入数字1：'))
num2 = int(input('请输入数字2：'))
result = sum_num(num1, num2)
print(result)
help(sum_num)
