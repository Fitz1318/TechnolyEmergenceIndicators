"""
对关键词进行预处理，
1.首先是收集某一年专利中的所有关键词并将其并入到一个列表中
2.对关键词进行统计次数，并以字典的形式保存下来
3.对关键词进行去重
4.将关键词保存成一个json文件，并记录下keywords和num
5.单独来一个文件保存去重后的关键词并保存下来
6.应该就是保存两个文件，这样方便日后用，一个是txt，一个是json

7.按照昨天的想法，是关键词和数量都分别放到一个txt中，然后变成一个字典，最后转换成json格式文件
"""
import itertools
import json
import collections

keyphrase_2015 = []
# 记录关键词
# 记录关键词对应数量
quchong_keyphrase_2015 = []
num = []
with open("../Raw Data/2020.json") as f:
    for line in f.readlines():
        data = json.loads(line)
        # print(type(data))
        # 这里有一个问题就是好多结果是没有关键词的
        if 'keywords' in data.keys():
            keyphrase = data['keywords'].split(";")
            for i in keyphrase:
                # keyphrase_2015.append(i.strip())
                keyphrase_2015.append(i.strip().lower())
print(len(keyphrase_2015))
obj = collections.Counter(keyphrase_2015)

quchong_keyphrase_2015.extend(obj)
num.extend(obj.values())
myDict = {}
print(obj)

# print(k, v)
obj = dict(obj)
print(obj)

# 将去重前的关键词和数量保存成json文件，格式为{Keyphrase:XX,Num:XX}
# 将关键词统一成小写的，然后保存在result文件夹下
# with open("../Keyphrase/json/2020.json", 'w', encoding='utf-8') as f:
#     json.dump(obj, f)
with open("../Keyphrase/result/2020.json", 'w', encoding='utf-8') as f:
    json.dump(obj, f)

# # 将去重后的关键词保存成txt文件
# with open("../Keyphrase/txt/2015.txt", 'w', encoding='utf-8') as f:
#     for i in quchong_keyphrase_2015:
#         f.write(str(i).strip()+'\n')
#
# # 将去重后的关键词对应的数量保存成txt文件
# with open("../Keyphrase/num_2015.txt", 'w', encoding='utf-8') as f:
#     for i in num:
#         f.write(str(i).strip()+'\n')


# title = data['title']
# print(title)
# print(line)
# print(json.loads(line))
# data = json.load(f)
