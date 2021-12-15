"""
对术语进行属于持久性过滤
1.一个术语必须在某一段时期内出现超过3次
2.一个术语必须在活跃期出现过至少7次

1.首先将2011-2020年的所有关键词聚集到一个列表中,||||||||||||||||最好还是键值对的方式，（key,num),
2.对这个总集合进行统计次数后再去重
3.出现次数低于3次的直接去掉
4.去掉2014-2020年的术语少于7次的

这样剩下来的术语就通过了持久性这一关
"""
import json
import os
from collections import Counter

import linecache
import json
# dict_2011是2011年术语集合，其他类似
data_2011 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 1))
data_2012 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 2))
data_2013 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 3))
data_2014 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 4))
data_2015 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 5))
data_2016 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 6))
data_2017 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 7))
data_2018 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 8))
data_2019 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 9))
data_2020 = json.loads(linecache.getline("../Keyphrase/data/2011_2020.json", 10))
print(data_2011)
print(data_2014)

dict_2011_2013 = dict(Counter(data_2011) + Counter(data_2012) + Counter(data_2013))
dict_2014_2020 = dict(
    Counter(data_2014) + Counter(data_2015) + Counter(data_2016) + Counter(data_2017) + Counter(data_2018) + Counter(
        data_2019) + Counter(data_2020))

dict_2014_2016 = dict(Counter(data_2014) + Counter(data_2015) + Counter(data_2016))
dict_2017_2018 = dict(Counter(data_2017) + Counter(data_2018))
dict_2019_2020 = dict(Counter(data_2019) + Counter(data_2020))
dict_2018_2020 = dict(Counter(data_2018) + Counter(data_2019) + Counter(data_2020))

N_4_6 = len(dict_2014_2016)
print("2014-2016年中所有术语的数量:::", N_4_6)
N_7_8 = len(dict_2017_2018)
print("2017-2018年中所有术语的数量:::", N_7_8)
N_9_10 = len(dict_2019_2020)
print("2019-2020年中所有术语的数量:::", N_9_10)
N_8_10 = len(dict_2018_2020)
print("2018-2020年中所有术语的数量:::", N_8_10)
# print(dict_2011_2013)
# print(dict_2014_2020)
# N_1_3是2011-2013年所有术语的数量
N_1_3 = len(dict_2011_2013)
print("2011-2013年中所有术语的数量:::", N_1_3)
# N_4_10是2014-2020年所有术语的数量
N_4_10 = len(dict_2014_2020)
print("2014-2020年中所有术语的数量:::", N_4_10)
# 对2011-2020中所有进行统计，删除小于3的术语
dict_2011_2020 = dict(Counter(dict_2011_2013) + Counter(dict_2014_2020))
print("2011-2020中术语频率大于等于3次的个数:::", len(dict_2011_2020))
# dict_3是2011-2020年中术语频率大于等于3次的术语
dict_3 = {key: value for key, value in dict_2011_2020.items() if value >= 3}
# print(len(dict_3))
# print(dict_3)
# dict_1_3是2011-2013中术语出现频率大于等于3次的术语
dict_1_3 = {key: value for key, value in dict_2011_2013.items() if value >= 3}
print("2011-2013年中术语频率大于等于3次的个数:::", len(dict_1_3))
print("2011-2013中术语频率大于等于3的具体是哪些术语")
print(dict_1_3)
# print(sorted(dict_3.items(),key=lambda x:x[1]))
# dict_4_10是2014-2020年中术语出现频率大于等于3次的术语
print(Counter(dict_1_3).most_common())
dict_4_10 = {key: value for key, value in dict_2014_2020.items() if value >= 3}
# print("2014-2020年中术语频率大于等于3次的个数:::", len(dict_4_10))
# dict_7是统计2014-2020年中术语频率大于等于7次的术语
dict_7 = {key: value for key, value in dict_2014_2020.items() if value >= 7}
# print(dict_7)
# print(len(dict_7))
with open("../Keyphrase/data/dict_7", 'w') as f:
    json.dump(dict_7, f)
