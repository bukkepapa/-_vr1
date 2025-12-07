import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

with open('cols_100_105.txt', 'w', encoding='utf-8') as f:
    for i in range(100, 110):
        if i < len(df.columns):
            col_name = df.columns[i]
            sample = df.iloc[0, i] if len(df) > 0 else "N/A"
            f.write(f"Index {i}: {col_name}\n")
            f.write(f"  Sample: {sample}\n")
            f.write("-" * 20 + "\n")

print("Dumped columns 100-110 to cols_100_105.txt")
