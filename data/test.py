from pandas import Series,DataFrame
import pandas as pd

data = {'name':['apple','pear','st'],
       'count':[3,2,9],
       'price':[10,9,8]}
df = DataFrame(data)
count = df['count'].shift(1)
price = df['price']

# print(df[['count', 'price']].max(axis=1))
print(DataFrame([count, price]).T.min(axis=1))