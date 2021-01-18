
# 定义全局变量
glo_num = 0
# 定义函数
def test1():
    # 声明全局变量
    global glo_num
    glo_num = 100
def test2():
    print(glo_num)
test1()
test2()

# 返回值作为参数传递
def num1():
    return 50
def num2(num):
    print(num)
result = num1()
num2(result)