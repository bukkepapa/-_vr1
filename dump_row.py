import pandas as pd

# Load order file
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

# Target product codes
target_codes = [61539, 62192]

# Find row
found_rows = df[df.iloc[:, 97].isin(target_codes)]
if found_rows.empty:
    found_rows = df[df.iloc[:, 97].astype(str).isin([str(c) for c in target_codes])]

with open('row_dump.txt', 'w', encoding='utf-8') as f:
    if not found_rows.empty:
        row = found_rows.iloc[0]
        f.write(f"Product Code: {row.iloc[97]}\n")
        f.write("-" * 40 + "\n")
        
        for i, val in enumerate(row):
            if pd.notna(val) and str(val).strip() != '':
                try:
                    col_name = df.columns[i]
                    f.write(f"Index {i}: [{col_name}] = {val}\n")
                except:
                    f.write(f"Index {i}: [Unknown] = {val}\n")
    else:
        f.write("Row not found.\n")

print("Row data dumped to row_dump.txt")
