from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([('a',2),('b',1),('c',3),('d',11),('a',9),('a',1)])
    rdd2 = rdd.sortBy(lambda x:x[1])
    print(rdd2.collect())

    rdd3 = rdd.sortBy(lambda x:x[0])
    print(rdd3.collect())