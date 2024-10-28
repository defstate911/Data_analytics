import matplotlib.pyplot as plt
import pandas as pd

file_path = 'cleaned_divan_prices_3.csv'
data = pd.read_csv(file_path)

prices = data['Price']
df = pd.DataFrame(data)
print(f"Средняя цена на диваны - {df['Price'].mean()}")
bins_sqrt = int(len(data)**0.5)

plt.hist(prices, bins=bins_sqrt, edgecolor='black')

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()
