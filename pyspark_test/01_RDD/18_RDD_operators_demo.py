from pyspark import SparkConf,SparkContext
import json

if __name__ == '__main__':
    conf = SparkConf().setAppName('test').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    file_rdd = sc.textFile('../data/input/order.text')
    json_rdd = file_rdd.flatMap(lambda line:line.split('|'))
    dict_rdd = json_rdd.map(lambda json_str:json.loads(json_str))
    print(dict_rdd.collect())
    # 筛选出北京的商品
    bj_objs_rdd = dict_rdd.filter(lambda obj:obj['areaName'] == '北京')
    result_rdd = bj_objs_rdd.map(lambda obj:obj['areaName'] + '_' + obj['category'])
    print(result_rdd.distinct().collect())
