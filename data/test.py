from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import datetime
import time

df = pd.read_csv('./data/sh510500.csv')
total = len(df)
print(total)

bin = np.arange(0,24,0.5)
cut = pd.cut(df['pcnt_real_time'], bins=bin, labels=bin[:-1], right=False)
counts = pd.value_counts(cut,sort=False)
sum_counts = total - counts.cumsum().to_frame()

print(sum_counts)

def jls_extract_def():
    ##绘制直方图
    fig, ax = plt.subplots()
    ax.hist(x=df['pcnt_real_time'],bins=100,
            color="steelblue",
            edgecolor="black",
            cumulative=True,
            histtype='step',
            density=True)
    # ax.set_ylim(ax.get_ylim()[::-1])
    
    twin_axes=ax.twinx() 
    twin_axes.set_ylim(ax.get_ylim()[::-1])
    
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    
    #添加x轴和y轴标签
    plt.xlabel("rate")
    plt.ylabel("case")
    
    #添加标题
    plt.title("分布")
    plt.show()