import os
import re

PROJECT_DIR = os.path.expanduser('~/projects/myboinc/')

def produce(regex):
    found_numbers = set()
    number_to_filename = dict()
    value_to_number = dict()

    for results_dir in [os.path.join(PROJECT_DIR, 'result'), os.path.join(PROJECT_DIR, 'upload')]
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
                            value_to_number.setdefault(val, full_path)
                    except Exception as e:
                        print(f"Can't read file {full_path}: {e}")

    expected_numbers = set(range(0, 2001))
    missing_numbers = sorted(expected_numbers - found_numbers)

    print("Missed squares:", missing_numbers)

    print("Dict (value -> square_number):")
    for val, number in value_to_number.items():
        print(f"{val} -> {number}")

transversal_re = re.compile(r'^Transversal_(\d{1,5})_')
dtransversal_re = re.compile(r'^DTransversal_(\d{1,5})_')

produce(transversal_re)
produce(dtransversal_re)