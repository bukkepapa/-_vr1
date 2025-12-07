import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

# Target product codes
target_codes = [61539, 62192]

# Find row
found_rows = df[df.iloc[:, 97].isin(target_codes)]
if found_rows.empty:
    found_rows = df[df.iloc[:, 97].astype(str).isin([str(c) for c in target_codes])]

if not found_rows.empty:
    row = found_rows.iloc[0]
    print(f"Inspecting row for Product Code {row.iloc[97]}")
    print("-" * 40)
    
    # Check range 95-105 individually
    for i in range(95, 106):
        if i < len(df.columns):
            col_name = df.columns[i]
            val = row.iloc[i]
            print(f"Index {i}: [{col_name}] = {val}")
else:
    print("Row not found.")
