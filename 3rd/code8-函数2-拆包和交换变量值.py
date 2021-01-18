
# 1、拆包
# 1.1 元组
def num():
    return 100,200
num1,num2 =num()
print(num1)
print(num2)
# 1.2 字典
dict1 = {'name':'xiaoming','age':20}
a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])
# 2、交换变量值
# 方法一：
a = 10
b = 20
c = 0
c = a
a = b
b = c
print(a)
print(b)
# 方法二：


