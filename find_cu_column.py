import pandas as pd

# Calculate CU column index
col_name = 'CU'
result = 0
for char in col_name:
    result = result * 26 + (ord(char) - ord('A') + 1)

cu_index = result - 1
print(f'{col_name} column = index {cu_index}')

# Check the column
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=0)
cols = df.columns.tolist()

print(f'\nColumn {cu_index}: {cols[cu_index] if len(cols) > cu_index else "N/A"}')

# Also check nearby columns
for i in range(max(0, cu_index - 2), min(len(cols), cu_index + 3)):
    print(f'Column {i}: {cols[i]}')
