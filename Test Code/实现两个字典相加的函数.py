dicta = {'a': 2, 'c': 3, 'f': 11}
dictb = {'a': 1, 'b': -2, 'f': -100}
dict1 = {'a': 2, 'f': 11, 'b': 3}
dict2 = {'a': 1, 'b': 8, 'f': -100}
dict3 = {"Polyaniline": 1, " Graphene nanoplatelet": 1, " Multi-walled carbon nanotube": 1}

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

# 实现字典中的值相减
def subDict(x, y):
    result = {}
    for key in x:
        result[key] = x[key] - y[key]
    return result

# 实现字典键值去无关的空格

print(addDict(dicta, dictb))
print(addDict(dict1, dict2))
print(subDict(dict1, dict2))
