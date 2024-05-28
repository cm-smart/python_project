from pyspark import SparkConf,SparkContext
from pyspark.storagelevel import StorageLevel
from defs import context_jieba,filter_words,create_words,user_words_map
from operator import add

conf = SparkConf().setAppName('analysis_apacheLog').setMaster('local[*]')
sc = SparkContext(conf=conf)

file_rdd = sc.textFile('../../data/input/apache.log')
split_rdd = file_rdd.map(lambda line:line.split(' '))

# 将其缓存
split_rdd.cache()

# TODO:当前网站被访问的次数
print("需求1，当前网站被访问的次数：",split_rdd.count())
# TODO：访问的用户数
users_rdd = split_rdd.map(lambda obj:(obj[1],1))
print("用户访问数以及每个用户访问的数量：",users_rdd.reduceByKey(lambda a, b: a + b).collect())
# TODO：有哪些ip访问了本网站
ip_rdd = split_rdd.map(lambda obj:(obj[0],1))
print("ip统计：",ip_rdd.reduceByKey(lambda a, b: a + b).collect())
# TODO：哪个页面访问量最高
page_rdd = split_rdd.map(lambda obj:(obj[4],1))
result = page_rdd.reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(5)
print("页面访问量排名：",result)
# 释放
split_rdd.unpersist()


