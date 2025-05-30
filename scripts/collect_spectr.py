import os
import re

BASE_DIR = os.path.expanduser('~/projects/myboinc')

transversal_re = re.compile(r'^Transversal_(\d{1,5})_')

found_numbers = set()
number_to_filename = dict()
value_to_number = dict()

for root, dirs, files in os.walk(BASE_DIR):
    for fname in files:
        match = transversal_re.match(fname)
        if match:
            number = int(match.group(1))
            found_numbers.add(number)
            full_path = os.path.join(root, fname)
            
            try:
                with open(full_path, 'r') as f:
                    content = f.read().strip()
                    first_line = next(filter(None, content.splitlines()))
                    val = int(first_line)
                    value_to_number.setdefault(val, number)
            except Exception as e:
                print(f"Can't read file {full_path}: {e}")

expected_numbers = set(range(0, 2000))
missing_numbers = sorted(expected_numbers - found_numbers)

print("Missed squares:", missing_numbers)

print("Dict (value -> square_number):")
for val, number in value_to_number.items():
    print(f"{val} -> {number}")