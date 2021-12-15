"""
测试两个字典进行相加
例如dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'c': 3}
Out: {'a': 1, 'b': 2, 'c': 3}

第二个是键相同的值进行相加，键不同的直接放到后面。
例如dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'c': 3}
Out: {'a': 3, 'b': 2, 'c': 3}
"""

"""
测试将一个字典的值变成负数
例如 data = {'a': 1, 'b': 2}
data2 = {'a': 1, 'b': 2}
"""
import json
from collections import Counter

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'c': 3}
# 第一种实现方式
print({**dict1, **dict2})
# 第二种实现方式
print(dict(Counter(dict1) + Counter(dict2)))

# 删除值不符合条件的项目
dict3 = dict(Counter(dict1) + Counter(dict2))
print(dict3)

# 测试数值变成负数
data = {'a': 1, 'b': 2}
var = {key: value*10 for key, value in data.items()}
print(type(var))
print(var)
