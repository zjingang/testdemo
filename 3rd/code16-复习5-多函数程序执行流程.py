
# 共⽤用全局变量
glo_num = 0
def test1():
    # 修改全局变量
    global glo_num
    glo_num = 100
def test2():
    print(glo_num)
test1()
test2()

# 返回值作为参数传递
def test1():
    return 100
def test2(num):
    print(num)
result = test1()
test2(result)