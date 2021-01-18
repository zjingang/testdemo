
# 1、求三个数的和
def sum(a, b, c):
    sum1 = a + b + c
    return sum1
result = sum(1, 2, 3)
print(result)

# 2、求三个数平均值
def sum_num(a, b, c):
    return a + b + c
def avg_num(a, b, c):
    num = sum_num(a, b, c)
    return num / 3
result = avg_num(1, 2, 3)
print(result)