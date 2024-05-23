import pandas as pd

path = 'data/student_excel.xlsx'
df = pd.read_excel(path,skiprows=2)
print(df)

# 检测空值
obj1 = df.isnull()
print(obj1)

obj2 = df['分数'].isnull()
print(obj2)

obj3 = df['分数'].notnull()
print(obj3)

# 查找有分数的所有行
df.loc[df['分数'].notnull(),:]
print(df)
# 删除掉全是空值的列
print(df.loc[:,df.isnull().all()])
cols_to_drop = df.loc[:,df.isnull().all()].columns
print(cols_to_drop)
df = df.drop(cols_to_drop,axis=1)
print(df)
# 删除掉全是空值的行
df = df.dropna(how='all')
print(df)

# 将分数列为空的填充为0分
df['分数'] = df['分数'].fillna(0)
print(df)

# 将姓名的缺失值填充
df['姓名'] = df['姓名'].fillna(method='ffill')
print(df)

# 将清洗好的excel保存
df.to_excel('data/student_excel_clean.xlsx',index=False)