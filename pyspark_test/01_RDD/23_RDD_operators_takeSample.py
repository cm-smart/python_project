from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd1 = sc.parallelize([1,2,3,4,5,6,7],2)
    # 随机抽样RDD的数据
    # 参数1：True表示运行取同一个数据，False表示不能取同一个数据
    # 参数2：抽样要几个数据
    # 随机数种子
    print(rdd1.takeSample(True,16))
    print(rdd1.takeSample(False, 16))
    print(rdd1.takeSample(False, 2))


