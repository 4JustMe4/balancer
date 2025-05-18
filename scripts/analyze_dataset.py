import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('../data/df_with_matrix.csv')  # или ваш файл

# Быстрая гистограмма по всем данным (можно также строить по train/test)
plt.figure(figsize=(8,5))
plt.hist(df['cpu_time'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Распределение cpu_time')
plt.xlabel('cpu_time')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

print(len(df))
