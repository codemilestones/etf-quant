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

item = []
for index, row in df.iterrows():
    item.append(row['open'])
    item.append(row['close'])
    item.append(row['high'])
    item.append(row['low'])
    if(i%5==4):
        print(item)
        item = []
        i = -1
    i += 1
