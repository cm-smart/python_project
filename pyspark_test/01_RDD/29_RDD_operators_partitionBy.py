from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd1 = sc.parallelize([('hadoop',1),('spark',1),('hello',1),('flink',1),('hadoop',1),('spark',1)])

    # mapPartitions是操作一个分区，在分区中先操作逻辑，然后一次性传输过去
    def process(key):
        if 'hadoop' == key or 'hello' == key:
            return 0
        if 'spark' == key:
            return 1
        return 2


    print(rdd1.partitionBy(3,process).glom().collect())


