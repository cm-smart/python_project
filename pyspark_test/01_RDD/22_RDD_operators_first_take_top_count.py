from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd1 = sc.parallelize([1,2,3,4,5,6,7],2)
    print(rdd1.first())

    # 获取前5个数据
    print(rdd1.take(5))

    # 先降序，然后再取前5个
    print(rdd1.top(5))

    # 计算RDD有多少条数据
    print(rdd1.count())


