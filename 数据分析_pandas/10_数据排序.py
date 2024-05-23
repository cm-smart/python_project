import pandas as pd

path = 'data/2018_北京天气.csv'
df = pd.read_csv(path)

df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
print(df)

# series的排序
obj1 = df['aqi'].sort_values()
print(obj1)
obj2 = df['aqi'].sort_values(ascending=False)
print(obj2)

# dataFrame排序
df = df.sort_values(by='aqi')
print(df)

# 多列排序
df = df.sort_values(by=['aqiLevel','bWendu'])
print(df)

# 分别指定升序和降序
df = df.sort_values(by=['aqiLevel','bWendu'],ascending=[True,False])
print(df)