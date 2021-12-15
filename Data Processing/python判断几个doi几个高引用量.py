import csv
import json
import pandas as pd

data = pd.read_csv("C:/Users/Fitz/Desktop/ESI_download/space science/top.csv", usecols=['DOI'], nrows=10)
data_top = pd.read_csv("C:/Users/Fitz/Desktop/ESI_download/space science/top.csv", usecols=['DOI']).T.values.tolist()[0]
data_highly = \
    pd.read_csv("C:/Users/Fitz/Desktop/ESI_download/space science/highly cited.csv", usecols=['DOI']).T.values.tolist()[
        0]
print(len(data_top))
print(data_top)
print(len(data_highly))
print(data_highly)

print("space science里面top和highly cited相同的数量以及百分比\n" + str(len(
    set(data_top) & set(data_highly))) + ":" + str(len(set(data_top) & set(data_highly)) / len(data_top)))
