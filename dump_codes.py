import pandas as pd

# Load inventory file
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=3, usecols=[2, 3, 4])
df_inv.columns = ['商品コード', '商品名', '倉庫在庫数']

# Print raw values first 20
print("Raw Product Codes (First 20):")
print(df_inv['商品コード'].head(20).tolist())

# Convert to string and print
df_inv['商品コード'] = df_inv['商品コード'].astype(str)
print("\nString Converted Product Codes (First 20):")
print(df_inv['商品コード'].head(20).tolist())

# Check for our target codes again
target_codes = ['61539', '62192']
print(f"\nSearching for {target_codes} in {len(df_inv)} rows:")
for code in target_codes:
    if code in df_inv['商品コード'].values:
        print(f"  FOUND: {code}")
    else:
        print(f"  NOT FOUND: {code}")

# Dump all codes to file for inspection
with open('inventory_codes.txt', 'w') as f:
    for code in df_inv['商品コード'].unique():
        f.write(f"{code}\n")
print("\nAll codes dumped to inventory_codes.txt")
