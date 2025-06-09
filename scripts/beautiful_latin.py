import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def lighten_color(color, amount=0.6):
    try:
        c = mcolors.cnames[color]
    except:
        c = color
    rgb = mcolors.to_rgb(c)
    white = np.array([1, 1, 1])
    return tuple(rgb + (white - rgb) * amount)

# dt 0
latin_square = np.array([
    [2, 1, 4, 3],
    [4, 3, 2, 1],
    [3, 4, 1, 2],
    [1, 2, 3, 4],
])

# dt 0
# latin_square = np.array([
#     [0, 3, 5, 2, 6, 4, 1],
#     [2, 1, 4, 6, 3, 0, 5],
#     [3, 4, 2, 1, 5, 6, 0],
#     [5, 6, 0, 3, 1, 2, 4],
#     [1, 0, 6, 5, 4, 3, 2],
#     [6, 2, 1, 4, 0, 5, 3],
#     [4, 5, 3, 0, 2, 1, 6]
# ])
# dt 13
# latin_square = np.array([
#     [0, 2, 4, 5, 6, 3, 1],
#     [3, 1, 5, 6, 2, 0, 4],
#     [1, 3, 2, 4, 5, 6, 0],
#     [4, 6, 1, 3, 0, 2, 5],
#     [5, 0, 6, 2, 4, 1, 3],
#     [6, 4, 0, 1, 3, 5, 2],
#     [2, 5, 3, 0, 1, 4, 6]
# ])
# dt 27
# latin_square = np.array([
#     [0, 2, 4, 5, 3, 6, 1],
#     [6, 1, 0, 4, 5, 2, 3],
#     [1, 5, 2, 6, 0, 3, 4],
#     [4, 6, 5, 3, 1, 0, 2],
#     [2, 3, 6, 0, 4, 1, 5],
#     [3, 4, 1, 2, 6, 5, 0],
#     [5, 0, 3, 1, 2, 4, 6]
# ])
# t 878 & dt 101
# latin_square = np.array([
#     [0, 9, 4, 8, 7, 6, 5, 2, 1, 3],
#     [6, 1, 5, 0, 8, 9, 2, 3, 4, 7],
#     [1, 0, 2, 9, 6, 4, 3, 8, 7, 5],
#     [7, 8, 0, 3, 9, 2, 1, 6, 5, 4],
#     [3, 6, 1, 2, 4, 7, 0, 5, 9, 8],
#     [2, 7, 8, 1, 0, 5, 4, 9, 3, 6],
#     [8, 5, 9, 7, 3, 0, 6, 4, 2, 1],
#     [4, 2, 3, 5, 1, 8, 9, 7, 6, 0],
#     [9, 3, 6, 4, 5, 1, 7, 0, 8, 2],
#     [5, 4, 7, 6, 2, 3, 8, 1, 0, 9]
# ])
# t 59154432 & dt 21301376
# latin_square = np.array( [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#     [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],
#     [2, 3, 1, 0, 6, 7, 4, 5, 10, 11, 9, 8, 14, 15, 12, 13],
#     [3, 2, 0, 1, 7, 6, 5, 4, 11, 10, 8, 9, 15, 14, 13, 12],
#     [4, 5, 7, 6, 3, 2, 0, 1, 12, 13, 15, 14, 9, 10, 11, 8],
#     [5, 4, 6, 7, 2, 3, 1, 0, 13, 12, 14, 15, 10, 9, 8, 11],
#     [6, 7, 5, 4, 0, 1, 3, 2, 14, 15, 12, 13, 11, 8, 9, 10],
#     [7, 6, 4, 5, 1, 0, 2, 3, 15, 14, 13, 12, 8, 11, 10, 9],
#     [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
#     [9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6],
#     [10, 11, 9, 8, 14, 15, 12, 13, 2, 3, 0, 1, 7, 6, 5, 4],
#     [11, 10, 8, 9, 15, 14, 13, 12, 3, 2, 1, 0, 6, 7, 4, 5],
#     [12, 13, 14, 15, 9, 8, 11, 10, 4, 5, 7, 6, 0, 1, 3, 2],
#     [13, 12, 15, 14, 8, 9, 10, 11, 5, 4, 6, 7, 1, 0, 2, 3],
#     [14, 15, 12, 13, 11, 10, 9, 8, 6, 7, 5, 4, 3, 2, 0, 1],
#     [15, 14, 13, 12, 10, 11, 8, 9, 7, 6, 4, 5, 2, 3, 1, 0],
# ])

highlight_coords = [(0,2), (1,1), (2,3), (3,0)]

n = latin_square.shape[0]
vmax = np.max(latin_square)
base_cmap = cm.get_cmap('tab10', vmax+1)
cell_size = 0.3

fig, ax = plt.subplots(figsize=(n*cell_size, n*cell_size), dpi=140)

for i in range(n):
    for j in range(n):
        value = latin_square[i, j]
        base_color = base_cmap(value)
        light_color = lighten_color(base_color, amount=0.6)
        rect = plt.Rectangle([j-0.5, i-0.5], 1, 1, facecolor=light_color, edgecolor='gray')
        ax.add_patch(rect)
        color = 'red' if (i, j) in highlight_coords else 'black'
        # color = 'black'
        ax.text(j, i, str(value),
                ha='center', va='center', color=color)

ax.set_xlim(-0.5, n-0.5)
ax.set_ylim(-0.5, n-0.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

plt.subplots_adjust(left=0.04, right=0.96, top=1, bottom=0)
plt.tight_layout(pad=0)
plt.show()
