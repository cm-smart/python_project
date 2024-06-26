from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize(["hadoop spark hadoop","spark hadoop hadoop","hadoop flink spark"])
    rdd2 = rdd.map(lambda line: line.split(' '))
    print("rdd2:",rdd2.collect())
    rdd3 = rdd.flatMap(lambda line:line.split(' '))
    print("rdd3:",rdd3.collect())