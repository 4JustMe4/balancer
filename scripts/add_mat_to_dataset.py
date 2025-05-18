import pandas as pd
import numpy as np
import os

df = pd.read_csv('../data/boinc_result_host_dataset.csv')

mat_feature_names = [f'mat_{i}_{j}' for i in range(10) for j in range(10)]

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
    num = (row['workunit_id'] - 742) % 100
    filename = f'latin10x10_task_{num}_DTransversal'

    mat = load_matrix(filename)
    df.loc[idx, mat_feature_names] = mat.flatten()

print(df.head())

df.to_csv('../data/df_with_matrix.csv', index=False)
