import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Пример исходной матрицы A (порядок n=3)
A = np.array([
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
])
n = A.shape[0]
B = A + n  # A+n

# Формируем удвоенную матрицу
top = np.hstack((A, B))
bottom = np.hstack((B, A))
C = np.vstack((top, bottom))

# Создаем картинку
fig, ax = plt.subplots(figsize=(6, 6))

# Для разноцветных блоков
for i in range(2 * n):
    for j in range(2 * n):
        # Определяем цвет по блоку
        if (i < n and j < n) or (i >= n and j >= n):
            color = '#ffcccc'  # светло-красный для A
        else:
            color = '#ccffcc'  # светло-зелёный для A+n
        rect = plt.Rectangle([j, 2 * n - i - 1], 1, 1, facecolor=color, edgecolor='black')
        ax.add_patch(rect)
        # Пишем значение
        ax.text(j + 0.5, 2 * n - i - 1 + 0.5, str(C[i, j]), ha='center', va='center', fontsize=14)

# Подписи блоков
ax.text(n / 2, 2 * n + 0.2, 'A', ha='center', va='bottom', fontsize=16, fontweight='bold', color='#cc3333')
ax.text(3 * n / 2, 2 * n + 0.2, 'A+n', ha='center', va='bottom', fontsize=16, fontweight='bold', color='#339933')
ax.text(n / 2, -0.5, 'A+n', ha='center', va='top', fontsize=16, fontweight='bold', color='#339933')
ax.text(3 * n / 2, -0.5, 'A', ha='center', va='top', fontsize=16, fontweight='bold', color='#cc3333')

ax.set_xlim(0, 2 * n)
ax.set_ylim(0, 2 * n)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
# plt.title('Построение латинского квадрата порядка 2n из квадрата порядка n')
plt.tight_layout()
plt.show()
