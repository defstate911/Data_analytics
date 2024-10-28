import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)
#print(data)
bins_sqrt = int(np.sqrt(num_samples))
plt.hist(data, bins=bins_sqrt)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Гистограмма для случайных данных")
plt.show()

