from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 和reduce一样，接受传入逻辑进行聚合，聚合是带有初始值的
    # 分区内聚合
    # 分区间聚合
    rdd1 = sc.parallelize([1,2,3],3)
    print(rdd1.fold(10, lambda a, b: a + b))


