import pandas as pd

# Test with actual logic change
print("TESTING NEW LOGIC: ORDER-BASED ALLOCATION")
print("=" * 80)

# Load inventory file
print("\n1. Loading inventory file...")
df_inv = pd.read_excel('速報倉庫在庫.xlsx', header=3, usecols=[2, 4])
df_inv.columns = ['商品コード', '倉庫在庫数']
df_inv['倉庫在庫数'] = pd.to_numeric(df_inv['倉庫在庫数'], errors='coerce').fillna(0).astype(int)
df_inv = df_inv.dropna(subset=['商品コード'])
df_inv['商品コード'] = df_inv['商品コード'].astype(str)

# Filter out product code 30126
df_inv = df_inv[df_inv['商品コード'] != '30126']
print(f"   Loaded {len(df_inv)} products (excluding 30126)")

# Load order file
print("\n2. Loading order file...")
df_order = pd.read_csv('o3306679.txt', encoding='shift_jis', sep='\t', header=0, usecols=[14, 15, 97, 118])
df_order.columns = ['顧客コード', '顧客名', '商品コード', '発注数量']
df_order['発注数量'] = pd.to_numeric(df_order['発注数量'], errors='coerce').fillna(0).astype(int)
df_order = df_order.dropna(subset=['商品コード'])
df_order['商品コード'] = df_order['商品コード'].astype(str)

# Filter out product code 30126
df_order = df_order[df_order['商品コード'] != '30126']
print(f"   Loaded {len(df_order)} order rows (excluding 30126)")

# Group orders by product code
print("\n3. Grouping orders by product code...")
order_summary = df_order.groupby('商品コード')['発注数量'].sum().reset_index()
order_summary.columns = ['商品コード', '受注合計数']
print(f"   Unique products in orders: {len(order_summary)}")

# NEW LOGIC: Merge based on ORDERS (right join on order_summary)
print("\n4. Merging (ORDER-BASED)...")
allocation_df = order_summary.merge(df_inv, on='商品コード', how='left')

# Fill missing inventory with 0
allocation_df['倉庫在庫数'] = allocation_df['倉庫在庫数'].fillna(0).astype(int)

# Calculate allocation
allocation_df['引当後在庫'] = allocation_df['倉庫在庫数'] - allocation_df['受注合計数']

print(f"   Merged {len(allocation_df)} products")
print("\nSample merged data:")
print(allocation_df.head(10))

# Find shortages
print("\n5. Finding shortages...")
shortage_df = allocation_df[allocation_df['引当後在庫'] < 0].copy()
print(f"   Found {len(shortage_df)} products with shortages")

if len(shortage_df) > 0:
    shortage_df['不足数'] = shortage_df['引当後在庫'].abs()
    print("\nShortage products:")
    print(shortage_df[['商品コード', '倉庫在庫数', '受注合計数', '不足数']])
    
    # Get customer info for first shortage product
    if len(shortage_df) > 0:
        first_product = shortage_df.iloc[0]['商品コード']
        print(f"\nCustomers who ordered product {first_product}:")
        customers = df_order[df_order['商品コード'] == first_product][['顧客コード', '顧客名']].drop_duplicates()
        print(customers)
