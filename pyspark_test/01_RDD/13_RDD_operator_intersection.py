from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 返回两个rdd的交集，返回一个新的rdd
    rdd1 = sc.parallelize([('a',1),('b',1)])
    rdd2 = sc.parallelize([('a',1),('c',1)])
    
    rdd3 = rdd1.intersection(rdd2)
    print("交集：",rdd3.collect())