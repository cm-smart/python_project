import pandas as pd

path = 'data/ratings.csv'
df = pd.read_csv(path)

# index的用途：
#     1.更方便数据查询
#     2.使用index可以获得性能提升
#     3.自动的数据对其功能
#     4.更多更强大的数据结构支持

print(df.head())
print(df.count())

df.set_index('userId',inplace=True,drop=False)
print(df.head())
print(df.index)

# 使用index的查询方法
obj1 = df.loc[500].head(5)
print(obj1)

# 使用column的condition查询方法
obj2 = df.loc[df['userId'] == 500].head()
print(obj2)
