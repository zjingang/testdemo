# 递归
# 3以内数字累加
def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num-1)
result = sum_numbers(3)
print(result)

# lambda表达式------语法：lambda 参数列表：表达式
# （1）函数
def fn1():
    return 200
print(fn1)
print(fn1())
# (2) lambda表达式
fn2 = lambda :100
print(fn2)
print(fn2())

# 计算a+b
# （1）普通实现
def add(a,b):
    return a + b
result = add(1,2)
print(result)
# (2)lambda实现
result = lambda a, b : a + b
print(result(1,2))

# lambda的参数形式
# 1、无参数
fn1 = lambda :100
print(fn1())
# 2、一个参数
fn2 = lambda a:a
print(fn2('hello python'))
# 3、默认参数
fn3 = lambda a, b, c = 100:a + b + c
print(fn3(50, 50))
# 4、可变参数'*args'
fn4 = lambda *args:args
print(fn4(10,20,30))
# 5、可变参数'**kwargs'
fn5 = lambda **kwargs:kwargs
print(fn5(name = 'python',age = 20))

# lambda的应用
# 1、带判断的lambda
fn1 = lambda a,b:a if a > b else b
print(fn1(1000,500))
# 2、列表数据按字典的key值排序
students = [
    {'name':'Tom','age':20},
    {'name':'Rose','age':19},
    {'name':'Jack','age':22}]
# 按'name'值升序排列
students.sort(key=lambda x:x['name'])
print(students)
# 按'name'值升序排列
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
# 按'age'值升序排列
students.sort(key=lambda x:x['age'])
print(students)

# 高阶函数
# 体验高阶函数
def sum_num(a, b, f):
    return f(a) + f(b)
result = sum_num(-1, 2, abs)
print(result)
def sum_num1(a, b, f):
    return f(a) + f(b)
result = sum_num1(1.2, 1.9, round)
print(result)

# 内置高阶函数
# 1、map（）----map（func，lst）
# 计算list1 序列中各个数字的2次方。
list1 = [1,2,3,4,5]
def func(x):
    return x**2
result = map(func,list1)
print(result)
print(list(result))
# 2、reduce(func,lst)--func必须有两个参数
import functools
list2 = [1,2,3,4,5]
def func(a,b):
    return a + b
result = functools.reduce(func,list2)
print(result)
# 3、filter（func，lst）--
