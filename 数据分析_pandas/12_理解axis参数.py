import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A','B','C','D']
)
print(df)

# 删除某一列
obj1 = df.drop('A',axis=1)
print(obj1)

# 删除某一行
obj2 = df.drop(1,axis=0)
print(obj2)

obj3 = df.mean(axis=0)
print(obj3)

obj4 = df.mean(axis=1)
print(obj4)