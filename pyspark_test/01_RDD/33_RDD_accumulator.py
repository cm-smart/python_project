from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10],2)

    # spark提供的累加器变量，参数是初始值
    acmlt = sc.accumulator(0)

    def map_func(data):
        global acmlt
        acmlt += 1

    rdd2 = rdd.map(map_func)

    # 缓存一下
    rdd2.cache()

    rdd2.collect()

    rdd3 = rdd2.map(lambda x:x)
    rdd3.collect()

    print(acmlt)


