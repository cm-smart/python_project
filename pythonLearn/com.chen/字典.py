tinydict = {'name':'chenmin','age':32,'class':'First'}
print("tinydict['name']:",tinydict['name'])
print("tinydict['age']:",tinydict['age'])

# 更新
tinydict['age'] = 30
# 添加
tinydict['school'] = 'runoob'
print(tinydict)
# 删除
temp = tinydict['name']
print(temp)
del temp
# print("temp:",temp)
print(tinydict)
del tinydict['name']
print(tinydict)
# 清空字典所有条目
# tinydict.clear()
print(tinydict)
# 删除字典
# del tinydict
print(tinydict)

size = len(tinydict)
print(size)

# 字典函数练习
dict1 = {"name":"陈敏","age":32}
temp = dict1.copy()
print(temp)
temp["name"] = "chenmin"
print("temp:",temp)
print("dict1:",dict1)

seq = ('google','runoob','taobao')
thisdict = dict.fromkeys(seq)
print(thisdict)
thisdict = dict.fromkeys(seq,10)
print(thisdict)

print(dict1.get("name"))
tuple = dict1.items()
print(tuple)