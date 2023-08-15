import pandas as pd
import numpy as np

file = 'data/car.csv'

df = pd.read_csv(file)

df_1 = df
df_1['year_exp'] = df_1['year']
df_1.index = df.index*25
last_idx = df_1.index[-1] + 1
df_expanded = df_1.reindex(range(last_idx))
df_expanded['year'] = df_expanded['year'].fillna(method='ffill')
df_expanded['year'] = df_expanded['year'].astype('int')
df_expanded = df_expanded.interpolate()

print(df_expanded)

df_expanded.to_csv('data/expandeds.csv')