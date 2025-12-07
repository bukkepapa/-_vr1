import pandas as pd

df = pd.read_excel('速報倉庫在庫.xlsx', header=3, nrows=3)

print('Column names:')
for i in range(min(6, len(df.columns))):
    print(f'  Index {i}: {df.columns[i]}')

print('\nFirst 3 rows (columns 0-5):')
print(df.iloc[:, :6])
