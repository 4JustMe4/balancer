import click
import datetime
import os
import random
import shutil
import subprocess
import time

TASKS_NUMBER = 100
SQUARE_SIZE = 10


def formatName(i, suff):
    n = SQUARE_SIZE * 2
    return f'../data/latin{n}x{n}_task_{i}_{suff}'


def isConevrtibleToNumber(square):
    for row in square:
        for element in row:
            try:
                int(element)
            except ValueError:
                return False
    return True


def isSquare(square):
    n = len(square)
    for row in square:
        if len(row) != n:
            return False
    return True


def verifyNumbers(square, n):
    for row in square:
        for value in row:
            if not isinstance(value, int):
                return False
            if value < 0 or n <= value:
                return False
    return True


def verifyRows(square, n):
    for i in range(n):
        if n != len(set(square[i])):
            return False
    return True


def verifyColumns(square, n):
    for j in range(n):
        if n != len(set([square[i][j] for i in range(n)])):
            return False
    return True


def verifyLatinSquare(square):
    if not isSquare(square):
        return False
    n = len(square)
    if not verifyNumbers(square, n) or not verifyRows(square, n) or not verifyColumns(square, n):
        return False
    return True


def printLatinSquare(square, filename):
    n = len(square)
    with open(filename, 'w') as f:
        f.write(str(n) + '\n')
        for i in range(n):
            f.write(' '.join([str(value) for value in square[i]]) + '\n')


def createDoubleSquare(square):
    result = []
    n = len(square)
    for i in range(n):
        result.append(square[i] + [value + n for value in square[i]])

    for i in range(n):
        result.append([value + n for value in square[i]] + square[i])

    return result


@click.command()
@click.option('--squares', default=TASKS_NUMBER, help='Number of squares for generation')
def create_tasks(squares):
    click.echo(f"{squares} will be created")
    with open(f'../data/latin{SQUARE_SIZE}x{SQUARE_SIZE}') as f:
        data = f.read().split('\n')

    # random.shuffle(data)
    currentNum = 0
    for i in range(len(data)):
        if i % 10 == 0 or squares < 10:
            click.echo(f"Creating {i + 1}")

        if len(data[i]) == SQUARE_SIZE**2:
            strSquare = [data[i][j*SQUARE_SIZE:j*SQUARE_SIZE+SQUARE_SIZE] for j in range(SQUARE_SIZE)]
            if not isConevrtibleToNumber(strSquare):
                click.echo(f"Ignore line {i + 1}. Can't convert some values to int")
                continue
            square = [[int(element) for element in row] for row in strSquare]

            if not verifyLatinSquare(square):
                click.echo(f"Ignore line {i + 1}. No valid latin square")
                continue

            for suff in ['Transversal', 'DTransversal']:
                doubelSquare = createDoubleSquare(square)
                if not verifyLatinSquare(doubelSquare):
                    click.echo(f"Can't create doubel square from {i + 1}")
                else:
                    f = os.path.abspath(formatName(currentNum // 2, suff))
                    printLatinSquare(doubelSquare, f)
                    currentNum += 1
            if currentNum >= 2 * squares:
                break
        else:
            click.echo(f"Ignore line {i + 1}. Unexpected length {len(data[i])}")

    cwd = os.getcwd()
    os.chdir('/home/boincadm/projects/myboinc')

    for name in ['Transversal', 'DTransversal']:
        click.echo(f"Register inputs for {name}")
        for i in range(squares):
            absPathFile = os.path.join(cwd, formatName(i, name))
            filename = os.path.basename(absPathFile)
            print(absPathFile, filename)
            shutil.copy(absPathFile, filename)
            result = subprocess.check_output(['bin/stage_file', filename]).decode()
            click.echo(f"Staging result for {name}: {result}")

            wu_name = f'{name}_{i}_{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")}'
            result = subprocess.check_output(['bin/create_work', '--appname', name, '--wu_name', wu_name, filename]).decode()
            click.echo(f"Creating result for {wu_name}: {result}")


if __name__ == '__main__':
    create_tasks()
