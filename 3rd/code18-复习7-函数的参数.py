
# 1、位置参数（第一个实际参数传给第一个形式参数。。。。。。。）
def user_info(name, age, gender):
    print(f'您的名字是{name}，您的年龄是{age}，您的性别是{gender}')
user_info('xiaoming',20,'男')
# 2、关键字参数
def user_info(name, age,gender):
    print(f'您的名字是{name}，您的年龄是{age}，您的性别是{gender}')
user_info('xiaoming',age = 20, gender = '男')
user_info('rose', gender = '女',age = 18)

# 缺省参数
def user_info(name, age, gender = '男'):
    print(f'您的名字是：{name}，年龄是：{age}，性别是：{gender}')
user_info('xiaogang', 20)
user_info('xiaohong',22,'女')
# 不定长参数
# 1、包裹位置传递（*args）
def user_info(*args):
    print(args)
user_info('xiaoming')
user_info('xiaohong',20)
list1 = [1, 2, 3]
user_info(*list1)
# 2、包裹关键字传递（**kwargs）
def user_info(**kwargs):
    print(kwargs)
user_info(name = 'xiaohong',age = 20, gender = '女')
dict1 = {'name':'xiaogang', 'age' : 20, 'gender' : '男'}
user_info(**dict1)
