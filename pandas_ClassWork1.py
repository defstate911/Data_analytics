import pandas as pd

#df = pd.read_csv('hh.csv')
#df['Test'] = [new for new in range(29)] # добавили столбец Тест
#print(df)
#df.drop('Test', axis=1, inplace=True) # удаляем столбец Тест
#print(df)
#df.drop(28, axis=0, inplace=True)
#print(df)

# эксперемент с другим датасетом
df = pd.read_csv('animal.csv')
print(df)
#df.fillna(value=0, inplace=True) # поменяли NaN на 0
#print(df)
#df.dropna(inplace=True)# удалили кошку илошадь из датасета, т.к. значения Nan
#print(df)
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
df.to_csv('output.csv', index=False)