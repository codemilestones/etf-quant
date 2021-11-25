#coding=UTF-8 

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import datetime
import time


# 计算网格风险值：市值稳定网格法的情况下
# 画一张图出来，根据网格的变化，求最大回撤，和网格范围

init_money = 15000
extra_money = 5000
current_price = 1
buy_stock = 0
buy_money = 200
steps = np.arange(0.1,5,0.1)

df = DataFrame()
for s in steps:
    price = current_price
    stock = init_money // (current_price * 100)
    left_money = extra_money

    if buy_stock == 0:
        once_money = buy_money
    else:
        once_money = buy_stock * price

    while left_money >= once_money and price > 0.01:
        price = price * (1 - s / 100)
        if buy_stock == 0:
            once_money = buy_money
        else:
            once_money = buy_stock * price

        if buy_stock == 0:
            stock += buy_money // (price * 100)
            left_money -= buy_money // (price * 100) * (price * 100)
        else:
            stock += buy_stock / 100
            left_money -= buy_stock * price
    
    back_rate = (stock*100*price + left_money) / (init_money + extra_money) * 100
    df[s] = [price, back_rate]

df = df.T
df.columns = ['last_price', '最大回撤']
