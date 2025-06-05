import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import readDataSet

# Загрузка данных
df = readDataSet()

# Быстрая гистограмма по всем данным (можно также строить по train/test)
plt.figure(figsize=(8,5))
plt.hist(df['cpu_time'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Распределение времени выполнения задач')
plt.xlabel('время выполнения')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

print(len(df))


# ---- АНАЛИЗ СРЕДНЕГО ВРЕМЕНИ ----
mean_cpu_time = df['cpu_time'][df['cpu_time'] > 0].mean()

# ---- КОЛИЧЕСТВО ОШИБОК ----
# Ошибка будем считать, например, outcome != 1 (BOINC: 1 -- success)
errors = df[df['success'] != 1].shape[0]
total   = df.shape[0]

# ---- ПРОМЕЖУТОК ВРЕМЕНИ ОТ ОТПРАВКИ ДО ФИНИША ----
first_sent_time = df['result_create_time'].min()
last_received_time = df['result_create_time'].max()  # Если есть 'received_time', лучше использовать его
if 'received_time' in df.columns and df['received_time'].notna().sum() > 0:
    last_received_time = df['received_time'].max()

# Превращаем в часы:
elapsed_hours = (last_received_time - first_sent_time) / 3600

# ---- ВЫВОД ----
# print(f"Задания workunit_id в диапазоне [{workunit_start}, {workunit_end}):")
print(f"- Среднее время cpu_time: {mean_cpu_time:.3f} сек")
print(df['cpu_time'][df['cpu_time'] > 0].min())
print(df['cpu_time'][df['cpu_time'] > 0].max())
print(f"- Количество ошибок (outcome != 1): {errors} из {total} ({errors*100/total:.2f}%)")
print(f"- Временной промежуток (от первого до последнего результата): {elapsed_hours:.2f} ч")

status_counts = df['success'].value_counts().sort_index()

# Подписи для секторов
labels = ['Неуспех', 'Успех']
sizes = [status_counts.get(0, 0), status_counts.get(1, 0)]
colors = ['salmon', 'skyblue']

# Круговая диаграмма
plt.figure(figsize=(5,5))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    counterclock=False
)
plt.title('Распределение успешности выполнения задач')
plt.axis('equal')  # Круговая форма
plt.tight_layout()
plt.show()
