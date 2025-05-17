import os
import random
import subprocess
import time


TASKS_NUMBER = 100
SQUARE_SIZE = 10


def formatName(i, suff):
    return f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}_task_{i}_{suff}'

with open(f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}') as f:
    data = f.read().split('\n')

# random.shuffle(data)
currentNum = 0
for i in range(len(data)):
    if i % 10 == 0:
        print(f'create task number {i}')
    square = data[i]
    if len(square) == SQUARE_SIZE**2:
        a = [square[i*SQUARE_SIZE:i*SQUARE_SIZE+SQUARE_SIZE] for i in range(SQUARE_SIZE)]

        for suff in ['Transversal', 'DTransversal']:
            f = os.path.abspath(formatName(currentNum, suff))
            with open(f, 'w') as output:
                output.write(f'{SQUARE_SIZE}\n')
                for row in a:
                    output.write(' '.join(row) + '\n')
        currentNum += 1
        if currentNum >= TASKS_NUMBER:
            break

cwd = os.getcwd()
os.chdir('/home/boincadm/projects/myboinc')

for name in ['Transversal', 'DTransversal']:
    for i in range(TASKS_NUMBER):
        result = subprocess.check_output(['bin/submit_job', name, os.path.join(cwd, formatName(i, suff))]).decode()
        print(result)
        time.sleep(1)