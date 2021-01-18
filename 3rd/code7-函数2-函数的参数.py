
#1、位置参数
def user_info(name,age,gender):
    print(f'您的名字是：{name},您的年龄是：{age}，性别是：{gender}')
user_info('xiaoming',20,'男')
#2、关键字参数------位置参数必须放在关键字参数的前面
def user_info(name, age, gender):
    print(f'您的名字是：{name},年龄是：{age}，性别是：{gender}')
user_info('ROSE',age = 20,gender = '女')
user_info('Tom',gender = '男',age = 20)
# 3、缺省参数
def user_info(name, age, gender='男'):
    print(f'您的名字是：{name},年龄是：{age}，性别是：{gender}')
user_info('xiaohong',20)
user_info('xiaoming', 20, '女')
#4、不定长参数
# 4.1 包裹位置传递------元组类型
def user_info(*args):
    print(args)
user_info('xiaoming')
user_info('xiaohong','女')
user_info()
list1 = [1, 2, 3]
user_info(*list1)     #-----传参时为名称时，需要加“*”号
# 4.2 包裹关键字传递------字典类型
def user_info(**kwargs):
    print(kwargs)
user_info(name= 'xiaoming',age=20,gender='男')
dict1 = {'name' : 'xiaohong', 'age' : 20, 'gender' : '女' }
user_info(**dict1)