import pandas as pd

# Load order file header only
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=0)

print("Searching for columns with '名' or '漢字'...")
print("-" * 40)

for i, col in enumerate(df.columns):
    if '名' in str(col) or '漢字' in str(col):
        print(f"Index {i}: {col}")

print("-" * 40)
print("Also checking columns around 97 (Product Code)...")
for i in range(95, 105):
    if i < len(df.columns):
        print(f"Index {i}: {df.columns[i]}")
