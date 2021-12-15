import json
import collections
from multidict import CIMultiDict
import re
keyphrase_2015 = []
# 记录关键词
# 记录关键词对应数量
# 解决了空格的问题，下一步需要解决的是忽略大小写的问题，感觉这个是一个错误，大小写应该是一样的才对
# 现在要尝试解决一下大小写的问题，将所有的单词都变成小写
quchong_keyphrase_2015 = []
num = []
with open("../Raw Data/2015.json") as f:
    for line in f.readlines():
        data = json.loads(line)
        # print(type(data))
        # 这里有一个问题就是好多结果是没有关键词的
        if 'keywords' in data.keys():
            keyphrase = data['keywords'].split(";")
            for i in keyphrase:
                keyphrase_2015.append(i.strip().lower())
            # print(keyphrase)
print(keyphrase_2015)
print(len(keyphrase_2015))
obj = collections.Counter(keyphrase_2015)

quchong_keyphrase_2015.extend(obj)
num.extend(obj.values())
myDict = {}
print(obj)
obj = dict(obj)
print(obj)




# 将去重前的关键词和数量保存成json文件，格式为{Keyphrase:XX,Num:XX}
with open("../Keyphrase/json/2015_new.json", 'w', encoding='utf-8') as f:
    json.dump(obj, f)
