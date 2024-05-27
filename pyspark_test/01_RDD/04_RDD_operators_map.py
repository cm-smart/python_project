from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1,2,3,4,5],3)

    def add(data):
        return data * 10

    result = rdd.map(add).collect()
    print(result)

    print(rdd.map(lambda data: data * 10).collect())