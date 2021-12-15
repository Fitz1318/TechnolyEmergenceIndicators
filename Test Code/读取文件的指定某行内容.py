"""
这里是读取文件的指定某行内容，使用json方式读出，这样可以变成字典类型，方便后面字典类型进行计算
"""
import linecache
import json
text = linecache.getline("../TestFile/test_C1.json", 2)
text = json.loads(text)
print(text)
print(type(text))

