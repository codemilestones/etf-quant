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


def compute_m_day_max(df, day):
    max_df = df['high']
    for i in range(0,day):
        max_df = DataFrame([df['high'].shift(i), max_df]).T.max(axis=1)
    return max_df

df = pd.read_csv('./data/sh510500.csv')


print(compute_m_day_max(df, 2000))



