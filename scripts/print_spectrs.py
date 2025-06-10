import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import readDataSet

def print(name, title, x):
    data = []
    with open(name) as f:
        records = f.read().split('\n')

    for r in records:
        number = int(r.split(' ')[0])
        cnt = int(r.split(' ')[1])
        for i in range(cnt):
            data.append(number)

    plt.figure(figsize=(8,5))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel('Количество квадратов с таким числом')
    plt.grid(True)
    plt.show()

print('../data/spectrT.txt', 'Распределение числа трансверсалей', 'Число трансверсалей')
print('../data/spectrDT.txt', 'Распределение числа диагональных трансверсалей', 'Число диагональных трансверсалей')