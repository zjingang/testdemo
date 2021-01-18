
# 递归
# 1、3以内数字累加和
num = int(input('请输入您想计算的数字：'))
def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)
result = sum_num(num)
print(result)

# 2、lambda表达式  语法：lambda 参数列表：表达式
# 2.1  基本函数调用
def fn1():
    return 100
print(fn1)
print(fn1())
# 2.2 lambda函数
fn2 = lambda : 100
print(fn2)
print(fn2())
# 3、计算a+b  （lambda表达式实现）
sum_add = lambda a,b: a+b
print(sum_add(10,20))
# 4、lambda应用
# 4.1 带判断的lambda
fn1 = lambda a,b:a if a > b else b
print(fn1(1000,500))
# 4.2 列表数据按字典key的值进行排序
students = [{'name':'xiaoming', 'age':20},
             {'name':'rose','age':19},
            {'name':'jack','age':22}
            ]
# 4.2.1 按name值升序排列
students.sort(key=lambda x:x['name'])
print(students)
# 4.2.2 按name值降序排列
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
# 4.2.3 按age值升序排列
students.sort(key=lambda x:x['age'])
print(students)

# 5、高阶函数
# 5.1 体验高阶函数
def sum_num(a,b,f):
    return f(a)+f(b)
result = sum_num(-1,2,abs)
print(result)
result = sum_num(1.2,1.5,round)
print(result)
# 5.2 内置高阶函数
# 5.2.1 map（func(函数名)，lst(序列名)）
list1 = [1,2,3,4,5,6]
def func(num):
    return num ** 2
result = map(func,list1)
print(result)
print(list(result))
# 5.2.2 reduce（func(函数名)，lst(序列名)） func函数必须有两个参数
# 例：计算list2中各元素的累加和
import functools
list2 = [1,2,3,4,5]
def sum_add(a,b):
    return a + b
result = functools.reduce(sum_add,list2)
print(result)
# 5.2.3 filter（func(函数名)，lst(序列名)） :过滤点不符合条件的元素
list3 = [1,2,3,4,5,6,7,8,9,10]
def sum(num):
    return num % 2 == 0
result = filter(sum,list3)
print(list(result))





