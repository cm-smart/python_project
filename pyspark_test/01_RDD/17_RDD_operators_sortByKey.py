from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([('a',2),('b',1),('c',3),('d',11),('a',9),('a',1)])

    print(rdd.sortByKey().collect())