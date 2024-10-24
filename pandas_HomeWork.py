import pandas as pd

df = pd.read_csv('songs_normalize.csv')
print(df.head())
print(df.info())
print(df.describe())

df1 = pd.read_csv('dz.csv')
group = df1.groupby('City')['Salary'].mean().reset_index()
group = group.rename(columns={'Salary': 'Average Salary'})
print(group)

