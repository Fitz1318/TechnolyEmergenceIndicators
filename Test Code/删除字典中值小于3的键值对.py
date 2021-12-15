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

mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 1}

var = {key: value for key, value in mydict.items() if value > 1}
print(type(var))
print(var)
