from pyspark import SparkConf,SparkContext
from pyspark.storagelevel import StorageLevel
from defs import context_jieba,filter_words,create_words,user_words_map
from operator import add

conf = SparkConf().setAppName('test').setMaster('local[*]')
sc = SparkContext(conf=conf)

file_rdd = sc.textFile('../../data/input/SogouQ.txt')
split_rdd = file_rdd.map(lambda line:line.split('\t'))

# 对split_rdd做缓存
split_rdd.persist(StorageLevel.DISK_ONLY)

# TODO:需求1：用户搜索关键词分析，寻找高频单词
content_rdd = split_rdd.map(lambda x:x[2])

words_rdd = content_rdd.flatMap(context_jieba)

# 过滤单词
filter_rdd = words_rdd.filter(filter_words)

# 替换单词
final_words_rdd = filter_rdd.map(create_words)
result = (final_words_rdd.reduceByKey(lambda a,b:a+b)
           # 降序排序，全局有效
          .sortBy(lambda x:x[1],ascending=False,numPartitions=1)
          .take(5))
print("需求1的结果：",result)

# TODO:需求2：用户id_搜索词，精确定位
user_words_rdd = split_rdd.map(lambda x:(x[1],x[2]))

final_user_words_rdd = user_words_rdd.flatMap(user_words_map)

result2 = final_user_words_rdd.reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(10)
print("需求2的结果：",result2)

# TODO:需求3：查看一天哪个小时段用户数量最多
hours_rdd = split_rdd.map(lambda x:(x[0].split(':')[0],1))
result3 = hours_rdd.reduceByKey(add).sortBy(lambda x:x[1],ascending=False,numPartitions=1).collect()
print(result3)



