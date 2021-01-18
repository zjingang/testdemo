
old_name = input('请输⼊入您要备份的⽂文件名：')
# 2.1 提取⽂文件后缀点的下标
index = old_name.rfind('.')
# print(index) # 后缀中.的下标
# print(old_name[:index]) # 源⽂文件名（无后缀）
# 2.2 组织新⽂文件名 旧⽂文件名 + [备份] + 后缀
new_name = old_name[:index] + '[备份]' + old_name[index:]
# 打印新⽂文件名（带后缀）
# print(new_name)
# 3.1 打开⽂文件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')
# 3.2 将源⽂文件数据写⼊入备份⽂文件
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
# 3.3 关闭⽂文件
old_f.close()
new_f.close()