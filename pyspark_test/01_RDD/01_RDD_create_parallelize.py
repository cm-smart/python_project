from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    # 构建SparkContext对象
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # 通过并行化集合方式创建RDD，本地集合 ->分布式对象（RDD）
    rdd = sc.parallelize([1,2,3,4,5,6,7,8,9])
    # 根据CPU核心来定的
    print("默认分区：",rdd.getNumPartitions())

    rdd = sc.parallelize([1,2,3],3)
    print("分区数：",rdd.getNumPartitions())
    # collect方法，是将RDD（分布式对象）中每个分区的数据，都发送到Driver中，形成一个Python list对象
    # 分布式 -> 本地集合
    print("rdd内容是：",rdd.collect())