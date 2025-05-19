import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('../data/df_with_matrix.csv')  # или ваш файл

# Быстрая гистограмма по всем данным (можно также строить по train/test)
plt.figure(figsize=(8,5))
plt.hist(df['cpu_time'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Распределение времени выполнения задач')
plt.xlabel('время выполнения')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

print(len(df))


# ---- НАСТРОЙКИ ----
csv_path = "df_with_matrix.csv"    # Ваш файл с результатами
workunit_start = 752
workunit_end = 952                # не включительно


# ---- ФИЛЬТР ПО ДИАПАЗОНУ ----
df = df[(df['workunit_id'] >= workunit_start) & (df['workunit_id'] < workunit_end)]

# ---- АНАЛИЗ СРЕДНЕГО ВРЕМЕНИ ----
mean_cpu_time = df['cpu_time'][df['cpu_time'] > 0].mean()

# ---- КОЛИЧЕСТВО ОШИБОК ----
# Ошибка будем считать, например, outcome != 1 (BOINC: 1 -- success)
errors = df[df['outcome'] != 1].shape[0]
total   = df.shape[0]

# ---- ПРОМЕЖУТОК ВРЕМЕНИ ОТ ОТПРАВКИ ДО ФИНИША ----
first_sent_time = df['result_create_time'].min()
last_received_time = df['result_create_time'].max()  # Если есть 'received_time', лучше использовать его
if 'received_time' in df.columns and df['received_time'].notna().sum() > 0:
    last_received_time = df['received_time'].max()

# Превращаем в часы:
elapsed_hours = (last_received_time - first_sent_time) / 3600

# ---- ВЫВОД ----
print(f"Задания workunit_id в диапазоне [{workunit_start}, {workunit_end}):")
print(f"- Среднее время cpu_time: {mean_cpu_time:.3f} сек")
print(f"- Количество ошибок (outcome != 1): {errors} из {total} ({errors*100/total:.2f}%)")
print(f"- Временной промежуток (от первого до последнего результата): {elapsed_hours:.2f} ч")
