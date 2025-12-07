import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

print("Searching for columns with '名' or '漢字'...")
print("-" * 40)

for i, col in enumerate(df.columns):
    if '名' in str(col) or '漢字' in str(col):
        # Print index and sample value
        sample = df.iloc[0, i] if len(df) > 0 else "N/A"
        print(f"MATCH FOUND at Index {i}")
        print(f"  Sample Value: {sample}")
        # Try to print column name, but handle error
        try:
            print(f"  Column Name: {col}")
        except:
            print("  Column Name: (Print Error)")
        print("-" * 20)
