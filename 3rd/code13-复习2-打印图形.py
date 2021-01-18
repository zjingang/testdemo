
# 打印一行横线
# 方法一：直接调用
def print_line():
    print('-' * 20)
# 调用函数
print_line()

# 方法二：返回值应用
# 定义函数
def print_line():
    # 返回值
    return '-' * 20
result = print_line()
print(result)
# 打印多行横线：循环方式
# 定义函数
def print_line():
    print('-' * 20)
def xunhuan(num):
    i = 0
    while i < num:
        print_line()
        i += 1
def print_lines(num):
    xunhuan(num)
print_lines(5)


