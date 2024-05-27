from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    file_rdd1 = sc.textFile('../data/input/words.txt')
    print("默认读取分区数：",file_rdd1.getNumPartitions())
    print("file_rdd1内容：",file_rdd1.collect())

    # 加最小分区数参数测试
    file_rdd2 = sc.textFile('../data/input/words.txt',3)
    file_rdd3 = sc.textFile('../data/input/words.txt',100)
    print("file_rdd2分区数",file_rdd2.getNumPartitions())
    print("file_rdd3分区数",file_rdd3.getNumPartitions())
