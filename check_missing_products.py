import pandas as pd

print("CHECKING FOR PRODUCTS IN INVENTORY FILE")
print("=" * 80)

# Load inventory file
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=3, usecols=[2, 3, 4])
df_inv.columns = ['商品コード', '商品名', '倉庫在庫数']
df_inv['商品コード'] = df_inv['商品コード'].astype(str)

# Check for specific codes
target_codes = ['61539', '62192']

print(f"Looking for codes: {target_codes}")
print("-" * 40)

found_count = 0
for code in target_codes:
    match = df_inv[df_inv['商品コード'] == code]
    if not match.empty:
        print(f"FOUND {code}:")
        print(match)
        found_count += 1
    else:
        print(f"NOT FOUND {code}")

print("-" * 40)
if found_count == 0:
    print("WARNING: None of the target codes were found in the inventory file.")
    print("This explains why the product name is empty if we only look in the inventory file.")
else:
    print("Some codes were found. If names are empty, check the '商品名' column content.")
