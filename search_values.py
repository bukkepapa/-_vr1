import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

print("Searching for values containing '伊藤園' or 'おーい' in the first 5 rows...")
print("-" * 40)

for r in range(min(5, len(df))):
    row = df.iloc[r]
    for i, val in enumerate(row):
        val_str = str(val)
        if '伊藤園' in val_str or 'おーい' in val_str:
            print(f"Row {r}, Index {i}: {val_str}")
            try:
                print(f"  Column Name: {df.columns[i]}")
            except:
                pass
            print("-" * 20)
