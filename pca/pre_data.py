#coding=UTF-8 

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import datetime
import time
import math

df = pd.read_csv('./data/sh510500.csv')

i = 0

total_df = pd.DataFrame().T
item=[]

with open("./pca/to_one.csv", "w") as text_file:
    text_file.write("")

for index, row in df.iterrows():
    item.append(row['open'])
    item.append(row['close'])
    item.append(row['high'])
    item.append(row['low'])
    if(i%5==4):
        df2 = pd.DataFrame(item)
        low = df2.min()
        high = df2.max()
        df2 = (df2 - low) / (high - low)
        with open("./pca/to_one.csv", "a") as text_file:
            ll =np.array(df2).reshape(1,-1).tolist()
            results = list(map(str, ll[0]))
            text_file.write(",".join(results) + '\n')
        item = []
        i = -1
    i += 1