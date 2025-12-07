import pandas as pd

# Analyze warehouse inventory file
print("WAREHOUSE INVENTORY FILE ANALYSIS")
print("=" * 60)

df = pd.read_excel('速報倉庫在庫.xlsx', header=3, nrows=5)
print(f"Total columns: {len(df.columns)}\n")

print("Column names:")
for i, col in enumerate(df.columns):
    print(f"  Index {i}: '{col}'")

print("\nFirst 3 rows of data:")
print(df.head(3))

print("\n" + "=" * 60)
print("Looking for product code and inventory columns...")
print("=" * 60)

# Check if columns C and E exist (indices 2 and 4)
if len(df.columns) > 4:
    print(f"\nColumn at index 2: '{df.columns[2]}'")
    print(f"Column at index 4: '{df.columns[4]}'")
    print("\nSample data:")
    print(df.iloc[:3, [2, 4]])
