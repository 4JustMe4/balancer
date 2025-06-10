import os
import re

PROJECT_DIR = os.path.expanduser('~/projects/myboinc/')

def produce(regex):
    found_numbers = set()
    number_to_filename = dict()
    numbers = dict()
    paths = dict()

    errors = 0
    for results_dir in [os.path.join(PROJECT_DIR, 'results'), os.path.join(PROJECT_DIR, 'upload')]:
        for root, dirs, files in os.walk(results_dir):
            for fname in files:
                match = regex.match(fname)
                if match:
                    number = int(match.group(1))
                    found_numbers.add(number)
                    full_path = os.path.join(root, fname)

                    try:
                        with open(full_path, 'r') as f:
                            content = f.read().strip()
                            first_line = next(filter(None, content.splitlines()))
                            val = int(first_line)
                            if val not in numbers:
                                numbers[val] = []
                                paths[val] = full_path

                            numbers[val].append(number)
                    except Exception as e:
                        errors += 1

    expected_numbers = set(range(0, 1000))
    missing_numbers = sorted(expected_numbers - found_numbers)

    print("Missed squares:", missing_numbers)

    print("Dict (value -> square_number):")
    for val, p in sorted(paths.items()):
        print(f"{val} -> {p} ({len(paths[val])})")

    print(f'There was {errors} errors with reading')
    with open('spectr.txt', 'a') as f:
        for val, number in sorted(numbers.items()):
            f.write(f"{val} {len(set(number))}")

transversal_re = re.compile(r'^multi_Transversal_(\d{1,5})_')
dtransversal_re = re.compile(r'^multi_DTransversal_(\d{1,5})_')

produce(transversal_re)
produce(dtransversal_re)