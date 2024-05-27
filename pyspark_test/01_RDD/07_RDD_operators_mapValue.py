from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([('a',2),('a',5),('b',2)])
    print(rdd.mapValues(lambda x:x * 10).collect())
    