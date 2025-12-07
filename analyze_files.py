import pandas as pd

print("=" * 80)
print("ANALYZING WAREHOUSE INVENTORY FILE")
print("=" * 80)

# Read warehouse inventory file
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=None)
print(f"\nFile shape: {df_inv.shape}")
print(f"Total rows: {df_inv.shape[0]}, Total columns: {df_inv.shape[1]}")

print("\n--- Row 3 (Expected header row) ---")
print(df_inv.iloc[3].tolist())

print("\n--- Row 4 (First data row) ---")
print(df_inv.iloc[4].tolist())

print("\n--- Row 5 (Second data row) ---")
print(df_inv.iloc[5].tolist())

# Now read with header=3
df_inv_with_header = pd.read_excel('速報倉庫在庫.xlsx', header=3)
print("\n--- Column names when using header=3 ---")
for i, col in enumerate(df_inv_with_header.columns):
    print(f"Index {i}: '{col}'")

print("\n--- First 3 rows of data ---")
print(df_inv_with_header.head(3))

print("\n" + "=" * 80)
print("ANALYZING ORDER FILE")
print("=" * 80)

# Read order file
df_order = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=None, nrows=3)
print(f"\nFile shape (first 3 rows): {df_order.shape}")
print(f"Total columns: {df_order.shape[1]}")

print("\n--- Row 0 (Expected header row) ---")
print(df_order.iloc[0].tolist())

print("\n--- Row 1 (First data row) ---")
print(df_order.iloc[1].tolist())

# Check specific columns mentioned in requirements
print("\n--- Checking specific column indices ---")
print(f"Column 14: {df_order.iloc[0, 14] if df_order.shape[1] > 14 else 'N/A'}")
print(f"Column 15: {df_order.iloc[0, 15] if df_order.shape[1] > 15 else 'N/A'}")
print(f"Column 97: {df_order.iloc[0, 97] if df_order.shape[1] > 97 else 'N/A'}")
print(f"Column 118: {df_order.iloc[0, 118] if df_order.shape[1] > 118 else 'N/A'}")

# Read with header
df_order_with_header = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, nrows=2)
print("\n--- First 2 data rows with header ---")
print(df_order_with_header.head(2))
