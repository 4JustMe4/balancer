import pandas as pd

beg = 2066
SIZE = 20
df = pd.read_csv(f'../data/df_with_matrix_{SIZE}_{beg}.csv')

split_idx = len(df) // 3
df1 = df.iloc[:split_idx]
df2 = df.iloc[split_idx:2*split_idx]
df3 = df.iloc[2*split_idx:]

df1.to_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part1.csv', index=False)
df2.to_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part2.csv', index=False)
df3.to_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part3.csv', index=False)