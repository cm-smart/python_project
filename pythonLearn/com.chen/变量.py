# 赋值整型变量
counter = 100
# 浮点型
miles = 1000.0
# 字符串
name = "chenmin"

print(counter)
print(miles)
print(name)

# 多变量赋值
a = b = c = 1
d, e, f = 1, 2, "john"
var1 = 1
var2 = 10
del var1, var2
# 字符串
str = "abcdef"
print(str[1:5])
print(str * 2)
print(str + "test")
# 列表
t = ['a','b','c','d','e']
print(t[1:3])
print(t[:4])
print(t[2:])
tinylist = [123,'john']
print(tinylist * 2)
print(t + tinylist)
# 元组
tuple = ("runoob",786,2.23,"john",70.2)
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
#字典
dict = {}
dict["one"] = "this is one"
dict[2] = "this is two"

tinydict = {"name":"runoob","code":6734,"dept":"sales"}
print(dict["one"])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
