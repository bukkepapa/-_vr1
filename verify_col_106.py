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
    print(f"Product Code: {row.iloc[97]}")
    print(f"Index 106 Value: {row.iloc[106]}")
    try:
        print(f"Index 106 Name: {df.columns[106]}")
    except:
        pass
else:
    print("Row not found.")
