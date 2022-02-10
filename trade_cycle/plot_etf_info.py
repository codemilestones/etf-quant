import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from pandas import Series,DataFrame
import pandas as pd
import math



def plot_etf_info(code, axe):
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    path = "../data/" + code + ".csv"
    data_df = pd.read_csv(path)
    lastDayData = data_df.tail(1)
    date = lastDayData.iloc[0].at['date']
    max_price = lastDayData.iloc[0].at['max_price']
    min_price = lastDayData.iloc[0].at['min_price']
    current_price = lastDayData.iloc[0].at['close']
    current_rate = (1 - (math.log(current_price) - math.log(min_price)) / (math.log(max_price) - math.log(min_price))) * 100

    # y=0.00010100750089083607x^3-0.0028596869977607696x^2+0.5242758923580495x+-1.2199225491198016
    recommend_position_rate = (math.pow(current_rate, 3) * 0.00008 - math.pow(current_rate, 2) * 0.00286 + current_rate * 0.524276) / 105 * 100

    user_df = pd.read_csv('../trade_cycle/current_trade.csv')
    select_code_data = user_df[user_df['code'] == code]
    name = select_code_data.iloc[0].at['name']
    cost_price = select_code_data.iloc[0].at['cost_price']
    total_cash = select_code_data.iloc[0].at['total_cash']
    position = select_code_data.iloc[0].at['position']
    real_position_rate = position * cost_price / total_cash * 100
    loss_rate = (cost_price - current_price) / cost_price * 100

    size = 4
    x = np.arange(size)
    a = np.arange(size)
    b = np.linspace(100,100,size)
    
    a[0] = current_rate
    a[1] = recommend_position_rate
    a[2] = real_position_rate
    a[3] = loss_rate / 15 * 100
    if (a[3] < 0):
        a[3] = 0
    if (a[3] > 100):
        a[3] = 100
    
    axe.bar(x, b, fc='darkorange')
    axe.bar(x, a, fc='steelblue')
    

    bar_num = [str(round(current_rate, 2))+'%/', str(round(recommend_position_rate, 2))+'%', str(round(real_position_rate, 2))+'%', str(round(loss_rate, 2)) + '%']
    for xx, yy in zip(x,a):
        axe.text(xx, yy, str(bar_num[xx]), ha='center')
        if (xx == 0):
            axe.text(xx, yy-3, current_price, ha='center')
        if (xx == 3):
            left_max_loss = round((min_price / current_price - 1) * 100, 2)
            axe.text(xx, yy-3, str(left_max_loss)+'%' , ha='center')
    
    top = [min_price, '100%', '100%', '15%']
    for xx, yy in zip(x,b):
        axe.text(xx, yy+3, str(top[xx]), ha='center')

    bottom = [max_price, '0%', '0%', '0%']
    for xx, yy in zip(x,b):
        axe.text(xx, -5, str(bottom[xx]), ha='center')
    
    label = ['价格', '建议仓位', '实际仓位', '建仓亏损']
    for xx, yy in zip(x,b):
        axe.text(xx, -10, label[xx], ha='center')

    for xx, yy in zip(x,b):
        axe.text(xx, -25, '', ha='center')
    
    # plt.legend()
    axe.axis('off')

    axe.set_title(date + ' ' + code + ' ' + name, y=1.02)
    # plt.show()

# 无持仓版本
def plot_etf_info_simple(code, name, axe):
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    path = "../data/" + code + ".csv"
    data_df = pd.read_csv(path)
    lastDayData = data_df.tail(1)
    date = lastDayData.iloc[0].at['date']
    max_price = lastDayData.iloc[0].at['max_price']
    min_price = lastDayData.iloc[0].at['min_price']
    current_price = lastDayData.iloc[0].at['close']
    current_rate = (1 - (math.log(current_price) - math.log(min_price)) / (math.log(max_price) - math.log(min_price))) * 100

    # y=0.00010100750089083607x^3-0.0028596869977607696x^2+0.5242758923580495x+-1.2199225491198016
    recommend_position_rate = (math.pow(current_rate, 3) * 0.00008 - math.pow(current_rate, 2) * 0.00286 + current_rate * 0.524276) / 105 * 100

    size = 2
    x = np.arange(size)
    a = np.arange(size)
    b = np.linspace(100,100,size)
    
    a[0] = current_rate
    a[1] = recommend_position_rate
    
    axe.bar(x, b, fc='darkorange')
    axe.bar(x, a, fc='steelblue')
    

    bar_num = [str(round(current_rate, 2))+'%/', str(round(recommend_position_rate, 2))+'%']
    for xx, yy in zip(x,a):
        axe.text(xx, yy, str(bar_num[xx]), ha='center')
        if (xx == 0):
            axe.text(xx, yy-3, current_price, ha='center')
        if (xx == 1):
            left_max_loss = round((min_price / current_price - 1) * 100, 2)
            axe.text(xx, yy-3, str(left_max_loss)+'%' , ha='center')
    
    top = [min_price, '100%']
    for xx, yy in zip(x,b):
        axe.text(xx, yy+3, str(top[xx]), ha='center')

    bottom = [max_price, '0%']
    for xx, yy in zip(x,b):
        axe.text(xx, -5, str(bottom[xx]), ha='center')
    
    label = ['价格', '建议仓位/期望最大亏损']
    for xx, yy in zip(x,b):
        axe.text(xx, -10, label[xx], ha='center')

    for xx, yy in zip(x,b):
        axe.text(xx, -25, '', ha='center')
    
    # plt.legend()
    axe.axis('off')

    axe.set_title(date + ' ' + code + ' ' + name, y=1.02)
    # plt.show()

