
# 局部变量
def testA():
    a = 100
    print(a)
testA()
# 全局变量
a = 100
def testB():
    print(a)
def testC():
    print(a)
testB()
testC()
# 修改testC的变量为200
a = 100
def testB():
    print(a)
def testC():
    a = 200
    print(a)
testB()
testC()
print(f'全局变量a={a}')
# 如何在函数体内部修改全局变量
a = 100
def testB():
    print(a)
def testC():
    #声明全局变量
    global a
    a = 200
    print(a)
testB()
testC()
print(f'全局变量a={a}')
