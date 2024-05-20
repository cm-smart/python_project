import pandas as pd

# 使用列表创建dataFrame
# data = [['google',10],['runoob',12],['wiki',13]]
# df = pd.DataFrame(data,columns=['site','age'])
# print(df)
#
# # 使用astype方法设置每列的数据类型
# df['site'] = df['site'].astype(str)
# df['age'] = df['age'].astype(float)
#
# print(df)

# 使用字典创建
# data = {'site':['google','runoob','wiki'],'age':[10,12,13]}
# df = pd.DataFrame(data)
# print(df)

data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}
# df = pd.DataFrame(data)
# print(df)
# # 返回第一行
# print(df.loc[0])
# # 返回第二行
# print(df.loc[1])
# # 返回第一行和第二行
# print(df.loc[[0,1]])

# 指定索引
df = pd.DataFrame(data,index=['day1','day2','day3'])
print(df)
# 通过索引查找数据
print(df.loc['day2'])

# 通过列名访问
print(df['calories'])

# 通过属性访问
print(df.calories)

# 访问单个元素
# print(df.loc['day1'].calories)
# print(df['calories'][0])
#
# print(df.loc['day1']['calories'])

# 添加新列
df['newColumn'] = [100,200,300]
print(df)