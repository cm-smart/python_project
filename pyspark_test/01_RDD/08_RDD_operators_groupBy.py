from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([('a', 2), ('a', 5), ('b', 2),('a',1)])
    # 按照谁分组就返回谁
    rdd2 = rdd.groupBy(lambda x:x[0])
    print(rdd2.collect())
    rdd3 = rdd2.map(lambda x:list(x[1]))
    print(rdd3.collect())