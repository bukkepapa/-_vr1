import pandas as pd

df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=0)
cols = df.columns.tolist()

print("Columns around index 95-105:")
for i in range(95, min(105, len(cols))):
    print(f'{i}: {cols[i]}')
