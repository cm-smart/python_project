import pandas as pd

path = 'data/2018_北京天气.csv'
df = pd.read_csv(path)
print(df.head())

# 设定索引为日期，方便按日期筛选
df.set_index('ymd',inplace=True)

print(df.index)

# 替换温度的后缀℃
df['bWendu'] = df['bWendu'].str.replace('℃',"").astype('int32')
df['yWendu'] = df['yWendu'].str.replace('℃',"").astype('int32')
print(df.head())
print(df.dtypes)

# 使用单个label值查询数据
# 得到单个值
print(df.loc['2018-01-03'].bWendu)
print(df.loc['2018-01-03','bWendu'])
obj = df.loc['2018-01-03',['bWendu','yWendu']]
print(obj)
print(type(obj))

# 使用值列表批量查询
obj2 = df.loc[['2018-01-03','2018-01-04','2018-01-05'],'bWendu']
print(obj2)
print(type(obj2))

# 使用数值区间进行范围查询
obj3 = df.loc['2018-01-03':'2018-01-05',['bWendu','yWendu']]
print(obj3)
print(type(obj3))

# 列index按区间
obj4 = df.loc[['2018-01-03','2018-01-04'],'bWendu':'fengxiang']
print(obj4)
print(type(obj4))

# 使用条件表达式
# 查询最低温度低于-10度的列表
obj5 = df.loc[df['yWendu'] < -10]
print(obj5)

# 复杂条件查询
# 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
obj6 = df.loc[(df['bWendu'] < 30) & (df['yWendu'] > 15) & (df['tianqi'] == '晴')
              & (df['aqiInfo'] == '优')]
print(obj6)

# 调用函数查询
# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
    return df.index.str.startswith('2018-09') & (df['aqiLevel'] == 1)
obj7 = df.loc[query_my_data(df)]
print(obj7)
print(df.index.str.startswith('2018-09'))