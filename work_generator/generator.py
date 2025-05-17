import os
import random
import subprocess
import time


TASKS_NUMBER = 50
SQUARE_SIZE = 10
BOINC_ROOT = '/home/boincadm/projects/myboinc'


def formatName(i):
    return f'latin{SQUARE_SIZE}x{SQUARE_SIZE}_task_{i}'

def getText(square):
    ans = f'{SQUARE_SIZE}\n'
    for row in square:
        ans += ' '.join(row) + '\n'
    return ans

cwd = os.getcwd()
os.chdir(BOINC_ROOT)

with open(os.path.join(cwd, f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}')) as f:
    data = f.read().split('\n')

# random.shuffle(data)
for i in range(TASKS_NUMBER):
    if i % 10 == 0:
        print(f'create task number {i}')
    square = data[i]
    if len(square) == SQUARE_SIZE**2:
        a = [square[i*SQUARE_SIZE:i*SQUARE_SIZE+SQUARE_SIZE] for i in range(SQUARE_SIZE)]

        f = os.path.abspath(os.path.join(cwd, '../data/', formatName(i)))
        with open(f, 'w') as output:
            output.write(getText(a))
        result = subprocess.check_output(['bin/stage_file', '--copy', f]).decode()

for name in ['Transversal', 'DTransversal']:
        files = [formatName(i) for i in range(TASKS_NUMBER)]
        result = subprocess.check_output(['bin/create_work', '--appname', name] + files).decode()
        print(result)
        time.sleep(1)
