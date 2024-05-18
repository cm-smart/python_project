import os

# 文件I/O操作
print("Python是一个非常棒的语言，不是吗？")

# str = input("请输入：")
# print("你输入的内容是：",str)

# 打开和关闭文件
fo = open("foo.txt","w")
print("文件名：",fo.name)
print("是否已关闭：",fo.closed)
print("访问模式：",fo.mode)

fo.write("www.runnoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

# 读取文件
fo = open("foo.txt","r+")
str = fo.read(10)
print("读取的字符串是：",str)

# 文件定位
position = fo.tell()
print("当前文件位置：",position)
#把指针再次重新定位到文件开头
position = fo.seek(0,0)
str = fo.read(10)
print("重新读取字符串：",str)

# 重命名和删除文件
# test1 = open("test1.txt","w")
# test1.close()
# os.rename("test1.txt","test2.txt")
# os.remove("test2.txt")

# 创建目录
# os.mkdir("newdir")

# 改变当前目录
# os.chdir("/home/newdir")

# 显示当前的工作目录
print(os.getcwd())

# 删除目录
os.rmdir("newdir")


# 关闭
fo.close()