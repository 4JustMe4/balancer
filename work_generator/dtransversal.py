import random
import os

TASKS_NUMBER = 100
SQUARE_SIZE = 10

with open(f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}') as f:
    data = f.read().split('\n')

random.shuffle(data)
for i in range(100):
    square = data[i]
    if len(square) == SQUARE_SIZE**2:
        a = [square[i*SQUARE_SIZE:i*SQUARE_SIZE+SQUARE_SIZE] for i in range(SQUARE_SIZE)]

        f = os.path.abspath(f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}_task_{i}')
        with open(f, 'w') as output:
            output.write(f'{SQUARE_SIZE}\n')
            for row in a:
                output.write(' '.join(row) + '\n')
