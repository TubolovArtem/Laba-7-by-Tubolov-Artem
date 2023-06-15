import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data2.csv')

column = data.columns[3]
values = data[column]
print(values)

# Гистограмма
plt.hist(values.values, bins=16)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Гистограмма data2.csv')
plt.show()

# Нормализованная гистограмма
plt.hist(values.values, bins=16, density=True)
plt.xlabel('Value')
plt.ylabel('Normalize')
plt.title('Норм. гистограмма data2.csv')
plt.show()

# Среднеквадратичное отклонение
std_dev = np.std(values.values)
plt.bar(range(16), values.mean(), yerr=std_dev)
plt.xlabel('Column')
plt.ylabel('Mean')
plt.title('СКО data2.csv')
plt.show()
