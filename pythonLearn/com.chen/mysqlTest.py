from pymysql import Connection

conn = Connection(
    host="node1",
    port=3306,
    user="root",
    password="cm021035"
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('test')

# 使用游标对象，执行sql语句
# cursor.execute('create table test_pymysql(id int,info varchar(50))')

# 插入
# try:
#     sql = "insert into test_pymysql(id,info) values (1,'hello')"
#     sql = "INSERT INTO test_pymysql(id,info) \
#            VALUES (%s, %s)" % \
#            (2, '测试')
#     cursor.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()

# 查询
# sql = 'select * from test_pymysql where id > %s' % (2)
# try:
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#
#     print(len(results))
#     for row in results:
#         id = row[0]
#         info = row[1]
#
#         print("id=%s,info=%s" % (id,info))
# except:
#     print("error:unable to fetch data")

# 更新
# sql = "update test_pymysql set info = 'update info' where id = %s" % (1)
# try:
#     cursor.execute(sql)
#     # 提交
#     conn.commit()
# except:
#     conn.rollback()

# 删除
sql = "delete from test_pymysql where id = %s" % (1)
try:
    cursor.execute(sql)
    # 提交
    conn.commit()
    print("删除成功")
except:
    conn.rollback()

# 关闭数据库
conn.close()
