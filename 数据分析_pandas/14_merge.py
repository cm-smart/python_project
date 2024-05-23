import pandas as pd

left = pd.DataFrame({
    'sno': [11, 12, 13, 14],
    'name': ['name_a', 'name_b', 'name_c', 'name_d']
})
print(left)

right = pd.DataFrame({
    'sno': [11, 12, 13, 14],
    'age': ['21', '22', '23', '24']
})
print(right)

# 一对一关系
obj1 = pd.merge(left, right, on='sno')
print(obj1)

# 一对多关系
right = pd.DataFrame({
    'sno': [11, 11, 11, 12, 12, 13],
    'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
})
obj2 = pd.merge(left,right,how='left',on='sno')
print(obj2)