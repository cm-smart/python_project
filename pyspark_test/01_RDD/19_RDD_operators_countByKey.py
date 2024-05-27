from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    file_rdd = sc.textFile('../data/input/words.txt')
    words_rdd = file_rdd.flatMap(lambda line:line.split(' '))
    print(words_rdd.collect())
    result_rdd = words_rdd.map(lambda word:(word,1))

    print(result_rdd.countByKey())

