"""
判断两个字典中相同的键，并修改字典，只保留有相同的键的键值对
"""

import json
import linecache
import math
from collections import Counter
import re

dict1 = {'a': 1, 'b': 2, 'f': 10}
dict2 = {'a': 2, 'c': 3, 'f': 11}
# new_dict1 = Counter(dict1)
# new_dict2 = Counter(dict2)
# print(type(new_dict1.subtract(new_dict2)))
# print(new_dict1.subtract(new_dict2))
# 这种方式就显示了相减，将其变成负数的过程
var3 = {key: value - 2 * value for key, value in dict1.items()}
var4 = dict(Counter(var3) + Counter(dict2))
print("var4是", var4)
print(var3)
c = dict1.keys() & dict2.keys()
print(c)
print(type(c))
var = {key: value for key, value in dict1.items() if key in c}
print(var)

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

keys_4_6 = data_2014.keys() & data_2015.keys() & data_2016.keys()
keys_8_10 = data_2018.keys() & data_2019.keys() & data_2020.keys()
keys_7_8 = data_2017.keys() & data_2018.keys()
keys_9_10 = data_2019.keys() & data_2020.keys()
# 4-10年竟然还真的是有关键词重复的。还有41个关键词重复
keys_4_10 = data_2014.keys() & data_2015.keys() & data_2016.keys() & data_2017.keys() & data_2018.keys() & data_2019.keys() & data_2020.keys()
print(len(keys_4_10))
# print(keys_4_6)
# print(len(keys_4_6))
# print(keys_8_10)
# print(len(keys_8_10))
# print(keys_7_8)
# print(len(keys_7_8))
# print(keys_9_10)
# print(len(keys_9_10))

# Active Trend
new_data_2014 = {key: value for key, value in data_2014.items() if key in keys_4_10}
new_data_2015 = {key: value for key, value in data_2015.items() if key in keys_4_10}
new_data_2016 = {key: value for key, value in data_2016.items() if key in keys_4_10}
new_data_2017 = {key: value for key, value in data_2017.items() if key in keys_4_10}
new_data_2018 = {key: value for key, value in data_2018.items() if key in keys_4_10}
new_data_2019 = {key: value for key, value in data_2019.items() if key in keys_4_10}
new_data_2020 = {key: value for key, value in data_2020.items() if key in keys_4_10}

dict_4_6 = dict(Counter(new_data_2014) + Counter(new_data_2015) + Counter(new_data_2016))
dict_8_10 = dict(Counter(new_data_2018) + Counter(new_data_2019) + Counter(new_data_2020))
dict_7_8 = dict(Counter(new_data_2017) + Counter(new_data_2018))
dict_9_10 = dict(Counter(new_data_2019) + Counter(new_data_2020))

dict_2014_2016 = dict(Counter(data_2014) + Counter(data_2015) + Counter(data_2016))
dict_2017_2018 = dict(Counter(data_2017) + Counter(data_2018))
dict_2019_2020 = dict(Counter(data_2019) + Counter(data_2020))
dict_2018_2020 = dict(Counter(data_2018) + Counter(data_2019) + Counter(data_2020))
N_4_6 = len(dict_2014_2016)
print("2014-2016年中所有术语的数量:::", N_4_6)
print(math.sqrt(N_4_6))
N_8_10 = len(dict_2018_2020)
print("2018-2020年中所有术语的数量:::", N_8_10)
print(math.sqrt(N_8_10))
N_7_8 = len(dict_2017_2018)
print("2017-2018年中所有术语的数量:::", N_7_8)
print(math.sqrt(N_7_8))
N_9_10 = len(dict_2019_2020)
print("2019-2020年中所有术语的数量:::", N_9_10)
print(math.sqrt(N_9_10))
N_7 = len(data_2017)
print("2017年术语的数量:::", N_7)
print(math.sqrt(N_7))
N_10 = len(data_2020)
print("2020年术语的数量:::", N_10)
print(math.sqrt(N_10))
add_4_6 = {key: value / math.sqrt(N_4_6) for key, value in dict_4_6.items()}
add_8_10 = {key: value / math.sqrt(N_8_10) for key, value in dict_8_10.items()}
add_7_8 = {key: value / math.sqrt(N_7_8) for key, value in dict_7_8.items()}
add_9_10 = {key: value / math.sqrt(N_9_10) for key, value in dict_9_10.items()}

add_7 = {key: value / math.sqrt(N_7) for key, value in new_data_2017.items()}
add_10 = {key: value / math.sqrt(N_10) for key, value in new_data_2020.items()}

print("4-6的长度", len(add_4_6))
print("8-10的长度", len(add_8_10))
print("7-8的长度", len(add_7_8))
print("9-10的长度", len(add_9_10))
"""
实现两个字典相减
1.首先将被减的字典的值-2倍值，这样就得到了对应的负值
2.使用Counter进行相加，这样加上一个负值就相当于两个字典相减
"""


def subDict(x, y):
    result = {}
    for key in x:
        result[key] = x[key] - y[key]
    return result


Active_Trend = subDict(add_8_10, add_4_6)
tmp = subDict(add_9_10, add_7_8)
Recent_Trend = {key: value * 10 for key, value in tmp.items()}

tmp2 = subDict(add_10, add_7)
Slope = {key: value / 3 * 10 for key, value in tmp2.items()}

double_Active_Trend = {key: value * 2 for key, value in Active_Trend.items()}


def addDict(x, y):
    result = {}
    for key in x:
        if y.get(key):
            result[key] = x[key] + y[key]
        else:
            result[key] = x[key]
    for key in y:
        if x.get(key):
            pass
        else:
            result[key] = y[key]
    return result


E1 = addDict(double_Active_Trend, Recent_Trend)
Escore = addDict(E1, Slope)

print("4—6的原值是", add_4_6)
print("8-10的原值是：", add_8_10)

print("8-10减去4-6", Active_Trend)
print("AT的长度", len(Active_Trend))
print("斜率的长度是：", len(Slope))
print("斜率是：", Slope)
print("分数的长度是：", len(Escore))
print("分数是:", Escore)

Escore_1 = {key: value for key, value in Escore.items() if value >= 0}
print("分数大于等于1.77", Escore_1)
print("最后结果的长度是：", len(Escore_1))
