import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
    }
df = pd.DataFrame(data)
df.to_csv('output1.csv', index=False) #создаем файл и туда сохраняем
print(df)

# Эксперимент с другим датасетом
#df = pd.read_csv('World-happiness-report-2024.csv')
#print(df.head()) # первые пять строк
#print(df.tail()) # последние строки
#print(df.info())
#print(df.describe()) # информация
#print(df['Country name'])
#print(df[['Country name', 'Regional indicator']])
#print(df.loc[56]) # 56 строка
#print(df.loc[56, 'Healthy life expectancy']) # в 56 строке столбец с этим названием
#print(df[df['Healthy life expectancy'] > 0.7]) # все показатели выше 0.7