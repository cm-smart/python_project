from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # glom加上嵌套，这个嵌套安分区来进行
    rdd = sc.parallelize([1,2,3,4,5],2)
    print(rdd.glom().collect())
