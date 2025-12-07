import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

print("Searching for specific column names...")
print("-" * 40)

targets = ['商品名', '漢字', '名称', '品名']

for i, col in enumerate(df.columns):
    for target in targets:
        if target in str(col):
            print(f"Index {i}: {col}")
            # Print sample value
            print(f"  Sample: {df.iloc[0, i]}")
            print("-" * 20)
