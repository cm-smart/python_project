import pandas as pd

path = 'data/2018_北京天气.csv'
df = pd.read_csv(path)

df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')

print(df.head())

# 直接赋值
def get_wendu_type(df):
    if df['bWendu'] > 33:
        return '高温'
    if df['yWendu'] < -10:
        return '低温'
    return '常温'
# 注意需要设置axis==1，这是series的index是columns
df['wendu_type'] = df.apply(get_wendu_type,axis=1)
print(df.head())

# 查看温度类型记数
obj1 = df['wendu_type'].value_counts()
print(obj1)

# 创建温差新列
def get_wencha_type(df):
    if df['bWendu'] - df['yWendu'] > 10:
        return '温差大'
    else:
        return '温差不大'
df['wencha_type'] = df.apply(get_wencha_type,axis=1)
print(df.loc[df['wencha_type'] == '温差大'])
print(df['wencha_type'].value_counts())


