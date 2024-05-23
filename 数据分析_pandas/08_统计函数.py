import pandas as pd

# 汇总类统计
# 唯一去重和安值计数
# 相关系数和协方差
path = 'data/2018_北京天气.csv'
df = pd.read_csv(path)
print(df.head(10))

# 替换掉温度
df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
print(df.head())
print(df.dtypes)

# 设定索引为日期，方便按日期筛选
df.set_index('ymd',inplace=True)

# 汇总类统计
# 一下子提取所有数字列统计结果
obj1 = df.describe()
print(obj1)

# 平均温度
obj2 = df['bWendu'].mean()
print(obj2)

# 最高温
obj3 = df['bWendu'].max()
print(obj3)
# 最低温
obj4 = df['bWendu'].min()
print(obj4)

# 唯一去重和按值计数
obj5 = df['fengxiang'].unique()
print(obj5)
# 按值计数
obj6 = df['fengxiang'].value_counts()
print(obj6)

# 相关系数和协方差
# 协方差：衡量同向反向程度，如果协方差为正，说明x,y同向变化，协方差越大说明同向程度越高；
#       如果协方差为负，说明x,y反向运动，协方差越小说明反向程度越高
# 相关系数：衡量相似程度，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，
#         当相关系数为-1时，说明两个变量变化的反向相似度最大
# 协方差矩阵
# obj7 = df.cov()
# print(obj7)

# 相关系数矩阵
# obj8 = df.corr()
# print(obj8)

# 单独查看空气质量和最高温度的相关系数
obj9 = df['aqi'].corr(df['bWendu'])
print(obj9)