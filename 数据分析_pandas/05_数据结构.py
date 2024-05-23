import pandas as pd
import numpy as np

# 使用数据列表产生简单的series
# s1 = pd.Series([1,'a',5.2,7])
# print(s1)
# print(s1.index)
# print(s1.values)
# 使用字典创建series
# sdata={'Ohio':35000,'Texas':72000,'Oregon':16000,'Utah':5000}
# s3 = pd.Series(sdata)
# print(type(s3))
# print(s3)
# print(s3[['Ohio','Texas']])
# print(type(s3[['Ohio','Texas']]))

# dataframe
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# print(type(df))
# print(df.index)

# 从DataFrame中查询出Series
# 如果只查询一行、一列，返回的是pd.Series
# 如果查询多行、多列，返回的是pd.DataFrame

# 查询一列
print(df['year'])
print(type(df['year']))
# 查询多列
print(df[['year','pop']])
print(type(df[['year','pop']]))
# 查询一行
print(df.loc[0])
print(type(df.loc[0]))
# 查询多行
print(df.loc[[0,1]])
print(type(df.loc[[0,1]]))