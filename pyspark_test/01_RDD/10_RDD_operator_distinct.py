from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 去重
    rdd = sc.parallelize([1,2,3,1,1,2,2,3])
    print(rdd.distinct().collect())

    rdd2 = sc.parallelize([('a',1),('b',2),('a',1),('b',1)])
    print(rdd2.distinct().collect())