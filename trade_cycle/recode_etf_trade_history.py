import math
import pandas as pd
import os

def compute_price_rate():
    max_price = 1.925
    min_price = 0.976
    current_price = 1.744
    percent = (1 - (math.log(current_price) - math.log(min_price)) / (math.log(max_price) - math.log(min_price))) * 100
    print(percent)


def record_trade_history(code):
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
    start_time = select_code_data.iloc[0].at['start_time']
    start_price = select_code_data.iloc[0].at['start_price']
    start_price_position = select_code_data.iloc[0].at['start_price_position']

    name = select_code_data.iloc[0].at['name']
    cost_price = select_code_data.iloc[0].at['cost_price']
    total_cash = select_code_data.iloc[0].at['total_cash']
    position = select_code_data.iloc[0].at['position']
    real_position_rate = position * cost_price / total_cash * 100
    loss_rate = (cost_price - current_price) / cost_price * 100

    output_path = '../trade_cycle/cycle_history/' + code + '_'+ name + '_' + start_time + '.csv'
    if os.path.exists(output_path):
        output_df = pd.read_csv(output_path, index_col=0)
    else:
        output_df = pd.DataFrame(columns=['date', 'code', 'name', 'start_time', 'start_price', 'start_price_position', 'cost_price', 'total_cash', 'position', 'real_position_rate', 'current_price', 'min_price', 'max_price','current_rate'])

    # 如果本日数据已更新，不追加数据
    if (len(output_df)>0 and output_df.tail(1).iloc[0].at['date']==date):
        return
    
    output_df = output_df.append([{
        'date': date, 
        'code': code,
        'name': name,
        'start_time': start_time,
        'start_price': start_price,
        'start_price_position': start_price_position,
        'cost_price': cost_price,
        'total_cash': total_cash,
        'position': position,
        'real_position_rate': real_position_rate,
        'current_price': current_price,
        'min_price': min_price,
        'max_price': max_price,
        'current_rate': current_rate}], ignore_index = True)

    output_df.to_csv(output_path)


