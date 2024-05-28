from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 仅支持硬盘存储
    # 被设计认为是安全的
    # 不保留血缘关系

    # 告知spark，开启CheckPoint功能
    sc.setCheckpointDir("hdfs://node1:8020/output/ckp")
    rdd1 = sc.textFile('../data/input/words.txt')
    rdd2 = rdd1.flatMap(lambda x:x.split(' '))
    rdd3 = rdd2.map(lambda x:(x,1))
    # 调用checkpoint api 保存数据
    rdd3.checkpoint()

    rdd4 = rdd3.reduceByKey(lambda a,b:a+b)
    print(rdd4.collect())

    rdd5 = rdd3.groupByKey()
    rdd6 = rdd5.mapValues(lambda x:sum(x))
    print(rdd6.collect())


