import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'E': ['E0', 'E1', 'E2', 'E3']
})

print(df1)

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7'],
    'F': ['F4', 'F5', 'F6', 'F7']
})

obj1 = pd.concat([df1,df2])
print(obj1)
# 使用ignore_index=True可以忽略原来的索引
obj1 = pd.concat([df1,df2],ignore_index=True)
print(obj1)
# 使用join=inner过滤掉不匹配的列
obj1 = pd.concat([df1,df2],ignore_index=True,join='inner')
print(obj1)

# 使用axis=1相当于添加新列
# 添加一列series
s1 = pd.Series(list(range(4)),name='F')
obj2 = pd.concat([df1,s1],axis=1)
print(obj2)