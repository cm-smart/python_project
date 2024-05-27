from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd1 = sc.parallelize([1,2,3,4,5,6],3)
    print(rdd1.reduce(lambda a, b: a + b))

