
# 打开文件并写入内容
# 语法：f = open(name(文件名)，mode)
# f = open('data.txt','w')
# f.write('hello world\n''123\n''321\n''1234567890\n''测试提升')
# f.close()
# 读文件内容
# 1、read
# f = open('data.txt')
# content = f.read(10)
# print(content)
# f.close()
# 2、readline
f = open('data.txt')
f.readline()
content = f.readline()
print(content)
content = f.readline()
print(content)
f.close()
# 3、readlines
f = open('data.txt')
content = f.readlines()
print(content)
f.close()
# seek():用来移动文件指针（光标）
# 文件对象.seek(偏移量，起始位置)
# f.seek(0)  表示光标调整到开始位置
# f.seek(1)  表示光标调整到当前位置
# f.seek(2)  表示光标调整到末尾位置

# 文件备份（格式：XXX[备份]后缀）
# 1、接收用户输入的文件名
old_name = input('请输入您的文件名：')
print(old_name)
# 2、备份文件名
# 2.1 提取目标文件后缀
index = old_name.rfind('.')
print(index)
print(old_name[:index])
# 2.2 组织备份文件名
new_name = old_name[:index]+'[备份]'+old_name[index:]
print(new_name)
# 3、文件内容写入备份文件
# 3.1 打开原文件和备份文件
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')
# 3.2 读取源文件内容并写入备份文件
# 这里采用循环一点一点读取文件内容避免文件太大，造成全部读取导致死机情况产生
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)
# 3.3 关闭文件
old_f.close()
new_f.close()
