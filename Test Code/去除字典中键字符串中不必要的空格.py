"""
将字典键中不应该存在的左侧的空格去除
妈的，暂时先不管了，把整个模型跑通一遍再说
不行啊，字典的键是唯一的，这个问题还是得去建立字典时去解决，现在这种情况下解决这个问题本身就不靠谱
"""

import json

dict3 = {"Polyaniline": 1, " Graphene nanoplatelet": 1, " Multi-walled carbon nanotube": 1}
# def removeBlank(x):
#     result = {key: value for key, value in x.items() key = key.strip()}}
#     return result