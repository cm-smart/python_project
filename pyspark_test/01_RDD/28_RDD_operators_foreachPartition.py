from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd1 = sc.parallelize([1,2,3,4,5,6,7],3)

    # mapPartitions是操作一个分区，在分区中先操作逻辑，然后一次性传输过去
    def process(data):
        result = list()
        for i in data:
            result.append(i * 10)
        print(result)


    print(rdd1.foreachPartition(process))


