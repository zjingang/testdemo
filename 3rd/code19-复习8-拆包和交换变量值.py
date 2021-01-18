
# 拆包
#1、 元组拆包
def num():
    return 10,20
num1,num2 = num()
print(num1)
print(num2)
# 2、字典拆包
dict1 = {'name':'xiaoming','age':20}
a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])

# 交换变量值
a,b = 10,20
a,b = b, a
print(a)
print(b)