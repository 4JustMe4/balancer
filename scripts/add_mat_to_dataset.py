import pandas as pd
import numpy as np
import os

beg = 2066
SIZE = 20
df = pd.read_csv('../data/boinc_result_host_dataset_{beg}.csv')

mat_feature_names = [f'mat_{i}_{j}' for i in range(SIZE) for j in range(SIZE)]

def load_matrix(filename):
    with open(f'../data/{filename}', 'r') as f:
        lines = f.readlines()
        size = int(lines[0].strip())
        matrix = []
        for line in lines[1:size+1]:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
        return np.array(matrix)

for idx, row in df.iterrows():
    number = int(row['workunit_name'].split('_')[1])
    filename = f'latin{SIZE}x{SIZE}_task_{number}_DTransversal'

    mat = load_matrix(filename)
    df.loc[idx, mat_feature_names] = mat.flatten()

df.drop('workunit_name', axis=1)

print(df.head())

df.to_csv('../data/df_with_matrix_{SIZE}_{beg}.csv', index=False)
