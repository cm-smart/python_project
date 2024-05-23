import pandas as pd

path = 'data/2018_北京天气.csv'
df = pd.read_csv(path)
print(df)
# 替换字符
# df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
# df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')

# 判断是不是数字
print(df['bWendu'].str.isnumeric())

condition = df['ymd'].str.startswith('2018-03')
print(condition)
print(df[condition])

df['ymd'] = df["ymd"].str.replace("-", "").str.slice(0, 6)
print(df['ymd'])
df["ymd"].str.replace("-", "").str[0:6]