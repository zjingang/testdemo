
# 求三个数之和
def sum_num(a, b, c):
    return a + b + c
a = int(input('please input num1:'))
b = int(input('please input num2:'))
c = int(input('please input num3:'))
result = sum_num(a, b, c)
print(result)

# 求三个数的平均数：方法一
def avg_num(num1, num2, num3):
    sumNum = num1 + num2 +num3
    return sumNum / 3
num1 = int(input('please input num1:'))
num2 = int(input('please input num2:'))
num3 = int(input('please input num3:'))
result = avg_num(num1, num2, num3)
print(result)

# 求三个数的平均数：方法二
def sum_num(a, b, c):
    return a + b + c
def avg_num(a, b, c):
    sum = sum_num(a, b, c)
    return sum / 3
result1 = avg_num(1,2,3)
print(result1)