import pandas as pd
from pymysql import Connection

# 读取纯文本文件
# path = 'data/2018_北京天气.csv'
# data = pd.read_csv(path)
# print("前5行：",data.head())
# # 查看数据的形状
# print("形状：",data.shape)
# # 查看列名
# print("列名：",data.columns)
# # 查看索引
# print("索引：",data.index)
# # 查看每列的数据类型
# print("数据类型：",data.dtypes)

# 读取txt文件，自己指定分隔符、列名
# path = 'data/access_pvuv.txt'
# data = pd.read_csv(path,sep='\t',header=None,names=['pdate','pv','uv'])
# print(data)

# 读取excel文件
# path = 'data/access_pvuv.xlsx'
# data = pd.read_excel(path)
# print(data)

# 读取mysql数据
conn = Connection(
    host="node2",
    port=3306,
    user="root",
    password="cm021035",
    database='test'
)
mysql_data = pd.read_sql('select * from app01_userinfo',con=conn)
print(mysql_data)
