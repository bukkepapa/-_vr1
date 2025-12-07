import pandas as pd

# Load order file
print("Loading order file...")
df = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0)

# Target product codes
target_codes = [61539, 62192]

print(f"\nSearching for rows with Product Code (index 97) in {target_codes}...")

# Filter rows
# Note: Column 97 is '商品コード' based on previous analysis
col_97_name = df.columns[97]
print(f"Column 97 name: {col_97_name}")

# Try to find the rows
found_rows = df[df.iloc[:, 97].isin(target_codes)]

if found_rows.empty:
    print("No rows found with integer comparison. Trying string comparison...")
    found_rows = df[df.iloc[:, 97].astype(str).isin([str(c) for c in target_codes])]

if not found_rows.empty:
    print(f"\nFound {len(found_rows)} rows.")
    row = found_rows.iloc[0]
    
    print("\nINSPECTING ROW DATA:")
    print("-" * 40)
    for i, val in enumerate(row):
        # Only print if value is not null/empty to reduce noise, or if it looks like a name
        if pd.notna(val) and str(val).strip() != '':
            print(f"Index {i}: [{df.columns[i]}] = {val}")
else:
    print("Could not find the target product codes in column 97.")
