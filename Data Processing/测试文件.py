import json

# 目前2015.json压根就不是一个json文件
# 但是现在这种做法好像也能勉强可以
with open("../Keyphrase/json/2015.json", 'r') as f:
    data = f.readline()
    print(data)
    print(type(data))
    data = json.loads(data)
    print(data)
    print(type(data))
    print('dye sensitized solar cells' in data.keys())
    print(data['dye sensitized solar cells'])
    if 'dye sensitized solar cells' in data.keys():
        print(data['dye sensitized solar cells'])




key = {}
num = {}
# 测试生成两个字典文件，之后在尝试将其合并
# with open("../Keyphrase/2015.txt",'r') as f:
#     for i in f.readlines():
#         key['keyphrase'] = i.strip('\n')
#         print(key)
#
# with open("../Keyphrase/num_2015.txt") as f_num:
#     for i in f_num.readlines():
#         num['num'] = i.strip('\n')
#         print(num)
#         d = {}
#         d.update(key)
#         d.update(num)
#         print(d)
# d = {}
# d.update(key)
# d.update(num)
# print(d)

d = {}
# 同时打开两个文件，做两个字典，然后合并两个字典成一个字典，最后再将字典变成json字符串
# with open("../Keyphrase/2015.txt",'r') as f1:
#     with open("../Keyphrase/num_2015.txt") as f2:
#         for i in f1.readlines():
#             key['keyphrase'] = i.strip('\n')
#         for i in f2.readlines():
#             num['num'] = i.strip('\n')
#             d.update(key)
#             d.update(num)
#             print(d)


