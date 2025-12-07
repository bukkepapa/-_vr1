import pandas as pd

df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=2)
cols = df.columns.tolist()

print(f"Total columns: {len(cols)}\n")

# Search for columns with "商品名" or "漢字"
print("Searching for product name columns:")
for i, col in enumerate(cols):
    if '商品名' in str(col) or '漢字' in str(col):
        print(f'  Index {i}: {col}')
        print(f'    Sample values: {df.iloc[:2, i].tolist()}')

# Also show columns 95-105
print("\nColumns 95-105:")
for i in range(95, min(105, len(cols))):
    print(f'{i}: {cols[i]}')
    if i < len(df.columns):
        print(f'   Sample: {df.iloc[0, i]}')
