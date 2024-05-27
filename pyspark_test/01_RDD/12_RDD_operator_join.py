from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 部门id和员工姓名
    x = sc.parallelize([(1001,'zhangsan'),(1002,'lisi'),(1003,'wangwu'),(1004,'zhangliu')])
    # 部门id和部门名称
    y = sc.parallelize([(1001,'sales'),(1002,'tech')])

    # 内连接
    rdd1 = x.join(y)
    print("内连接：",rdd1.collect())
    # 左外连接
    rdd2 = x.leftOuterJoin(y)
    print("左外连接：",rdd2.collect())
    # 右外连接
    rdd3 = x.rightOuterJoin(y)
    print("右外连接：",rdd3.collect())