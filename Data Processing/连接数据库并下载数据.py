"""
连接数据库并对标题和摘要中出现的候选术语挖掘进行下载数据并保存成json格式的文件
"""
import json
import re
from pymongo import MongoClient

client = MongoClient(host="mongodb://192.168.6.167:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")

dbList = client.list_database_names()
Db = client['wos']
myCollections = Db['publication_wos']
x = myCollections.find_one()
print(x)
# myQuery = {"year": 2015, "title": {"$regex": 'Dye Sensitized'}}
# or条件查询的方法
# condition = {"$or": [{"age": {"$gt": 22}}, {"name": {"$regex": "user"}}]}
# 不区分大小写
# myQuery = {"year": 2015, "title": re.compile('dye sensitized', re.IGNORECASE)}
myQuery = {"year": 2009, "$or": [{"title": re.compile('dye sensitized', re.IGNORECASE)},
                                 {"abstract": re.compile('dye sensitized', re.IGNORECASE)}]}

myDoc = myCollections.find(myQuery)
#
# for x in myDoc:
#     print(x)

with open('../Raw Data/2009.json', 'a', encoding='utf-8') as f:
    for x in myDoc:
        x['_id'] = str(x['_id'])
        x['ts'] = str(x['ts'])
        f.write(json.dumps(x) + '\n')
