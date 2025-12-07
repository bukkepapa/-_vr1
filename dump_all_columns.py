import pandas as pd

# Load order file header only
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=0)

with open('all_columns.txt', 'w', encoding='utf-8') as f:
    for i, col in enumerate(df.columns):
        f.write(f"{i}: {col}\n")

print("All columns dumped to all_columns.txt")
