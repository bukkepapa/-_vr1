import pandas as pd

print("DETAILED COLUMN ANALYSIS")
print("=" * 80)

# Read inventory file with header
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=3)

print("\nColumn names with indices:")
for i, col in enumerate(df_inv.columns):
    print(f"  {i}: '{col}'")

print("\n" + "=" * 80)
print("FIRST 3 ROWS OF DATA")
print("=" * 80)
print(df_inv.head(3))

print("\n" + "=" * 80)
print("CHECKING SPECIFIC COLUMNS")
print("=" * 80)

# Check what we're currently reading (columns at index 2 and 4)
print("\nCurrently reading:")
print(f"  Index 2 (C column): '{df_inv.columns[2]}'")
print(f"  Index 4 (E column): '{df_inv.columns[4]}'")

print("\nSample values from these columns:")
print(df_inv.iloc[:5, [2, 4]])

# Look for the actual inventory column
print("\n" + "=" * 80)
print("SEARCHING FOR INVENTORY COLUMN")
print("=" * 80)

for i, col in enumerate(df_inv.columns):
    if '在庫' in str(col):
        print(f"  Found at index {i}: '{col}'")
        print(f"  Sample values: {df_inv.iloc[:3, i].tolist()}")
