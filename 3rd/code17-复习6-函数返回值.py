
# 两个return情况
def test1():
    return 10
    return 20
result = test1()
print(result)
# 有多个返回值时，以元组形式输出
def test2():
    return 1,2
result = test2()
print(result)