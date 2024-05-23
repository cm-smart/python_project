import pandas as pd

df = pd.read_csv('data/nba.csv')

print(df.to_string())

# 读取前5行
print(df.head())
# 读取前面10行
print(df.head(10))
# 读取末尾5行
print(df.tail())
# 读取末尾10行
print(df.tail(10))

# 返回表格的一些基础信息
print(df.info())