import pandas as pd

file = 'archive/car_models.csv'

df = pd.read_csv(file)

df = df.transpose()



print(df)

df.to_csv('data/car.csv')