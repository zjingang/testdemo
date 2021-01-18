
# 1、局部变量--只在函数体内部生效
def testA():
    a = 100
    print(a)
testA()
# 2、全局变量--在函数体内外都生效的变量
# 定义全局变量
a = 100
def testA():
    print(a)
def testB():
    print(a)
testA()
testB()
# 3、testB 函数需求修改变量a的值为200
a = 100
def teatA():
    print(a)
def testB():
    a = 200
    print(a)
testA()
testB()
# 4、在函数体内部修改全局变量
a = 100
def testA():
    print(a)
def testB():
    global a
    a = 200
    print(a)
testA()
testB()
print(f'全局变量a = {a}')



