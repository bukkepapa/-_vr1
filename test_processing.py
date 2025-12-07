import pandas as pd

print("TESTING FULL DATA PROCESSING")
print("=" * 60)

# Load inventory file
print("\n1. Loading inventory file...")
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=3, usecols=[2, 4])
df_inv.columns = ['商品コード', '倉庫在庫数']
print(f"   Loaded {len(df_inv)} rows")
print(f"   商品コード dtype: {df_inv['商品コード'].dtype}")
print(f"   倉庫在庫数 dtype: {df_inv['倉庫在庫数'].dtype}")
print("\n   Sample data:")
print(df_inv.head(3))

# Convert inventory to int
df_inv['倉庫在庫数'] = pd.to_numeric(df_inv['倉庫在庫数'], errors='coerce').fillna(0).astype(int)
df_inv = df_inv.dropna(subset=['商品コード'])
print(f"\n   After cleaning: {len(df_inv)} rows")

# Load order file
print("\n2. Loading order file...")
df_order = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, usecols=[14, 15, 97, 118])
df_order.columns = ['顧客コード', '顧客名', '商品コード', '発注数量']
print(f"   Loaded {len(df_order)} rows")
print(f"   商品コード dtype: {df_order['商品コード'].dtype}")
print(f"   発注数量 dtype: {df_order['発注数量'].dtype}")
print("\n   Sample data:")
print(df_order.head(3))

# Convert order quantity to int
df_order['発注数量'] = pd.to_numeric(df_order['発注数量'], errors='coerce').fillna(0).astype(int)
df_order = df_order.dropna(subset=['商品コード'])
print(f"\n   After cleaning: {len(df_order)} rows")

# Group orders by product code
print("\n3. Grouping orders by product code...")
order_summary = df_order.groupby('商品コード')['発注数量'].sum().reset_index()
order_summary.columns = ['商品コード', '受注合計数']
print(f"   Unique products in orders: {len(order_summary)}")
print("\n   Sample grouped data:")
print(order_summary.head(3))

# Check data types before merge
print("\n4. Checking data types before merge...")
print(f"   Inventory 商品コード dtype: {df_inv['商品コード'].dtype}")
print(f"   Order 商品コード dtype: {order_summary['商品コード'].dtype}")

# Convert both to string for safe merging
print("\n5. Converting product codes to string...")
df_inv['商品コード'] = df_inv['商品コード'].astype(str)
order_summary['商品コード'] = order_summary['商品コード'].astype(str)

# Merge
print("\n6. Merging data...")
allocation_df = df_inv.merge(order_summary, on='商品コード', how='left')
allocation_df['受注合計数'] = allocation_df['受注合計数'].fillna(0).astype(int)
allocation_df['引当後在庫'] = allocation_df['倉庫在庫数'] - allocation_df['受注合計数']

print(f"   Merged {len(allocation_df)} rows")
print("\n   Sample merged data:")
print(allocation_df.head(5))

# Find shortages
print("\n7. Finding shortages...")
shortage_df = allocation_df[allocation_df['引当後在庫'] < 0]
print(f"   Found {len(shortage_df)} products with shortages")

if len(shortage_df) > 0:
    print("\n   Shortage products:")
    print(shortage_df)
