import pandas as pd

# a = [1,2,3]
# myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])

# a = ["Google","Runoob","Wiki"]
# myvar = pd.Series(a,index=["x","y","z"])
# print(myvar)
# print(myvar['y'])

# sites = {1:'Google',2:'Runoob',3:'Wiki'}
# myvar = pd.Series(sites)
# print(myvar)

# sites = {1:'Google',2:'Runoob',3:'Wiki'}
# myvar = pd.Series(sites,index=[1,2])
# print(myvar)

# 指定索引创建Series
s = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s)
# 获取值
# 获取索引为2的值
# value = s[2]
# print(value)
# 返回索引标签a对应的元素
# print(s['a'])
# 获取索引为1到3的值
# subset = s[1:4]
# print(subset)

# print('items:',s.items())
# 索引和值的对应关系
# for index,value in s.items():
#     print(index,value)

# 返回索引标签'a'到'c'之间的元素
# print(s['a':'c'])
# 返回前3个元素
# print(s[:3])

# 为特定的索引标签赋值
# s['a'] = 10

# 通过赋值给新的索引标签来添加元素
# s['e'] = 5
# print(s)

# 使用del删除指定索引标签的元素
# del s['a']
# 使用drop方法删除一个或多个索引标签，并返回一个新的SEries
# s_dropped = s.drop(['b','c'])
# print(s_dropped)
# print(s)

# result = s * 2
# print(result)

# 选择大于2的元素
# filter_series = s[s>2]
# print(filter_series)

# print(s.sum())
# # 平均值
# print(s.mean())
# print(s.max())
# print(s.min())
# # 标准差
# print(s.std())

# 属性和方法
# 获取索引
index = s.index
print(type(index))
print(index)
# 获取值
values = s.values
print(values)

# 获取描述统计信息
# stats = s.describe()
# print(stats)

# 获取最大值和最小值的索引
# max_index = s.idxmax()
# min_index = s.idxmin()
# print(min_index,max_index)

# 数据类型
print(s.dtype)
# 形状
print(s.shape)
# 元素个数
print(s.size)
print(s.head())
print(s.tail())