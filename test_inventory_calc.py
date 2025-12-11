
import pandas as pd
import numpy as np

def test_calculation():
    # Mock data representing [保管場所, 商品コード, 入数, 倉庫在庫数, 入庫予定]
    data = {
        '保管場所': ['A309001', 'A309001', 'OTHER', 'A309001'],
        '商品コード': ['111', '222', '333', '444'],
        '入数': [10, 12, 10, 6],
        '倉庫在庫数': [100, 50, 200, 10],
        '入庫予定': [5, 0, 10, 2]
    }
    
    df = pd.DataFrame(data)
    
    # Simulate the logic in app.py
    
    # Filter location
    df = df[df['保管場所'] == 'A309001']
    
    # Convert to numeric
    for col in ['倉庫在庫数', '入数', '入庫予定']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Calculation
    # Expected for 111: 100 + (5 * 10) = 150
    # Expected for 222: 50 + (0 * 12) = 50
    # Expected for 444: 10 + (2 * 6) = 22
    
    df['倉庫在庫数'] = df['倉庫在庫数'] + (df['入庫予定'] * df['入数'])
    
    print("Result DataFrame:")
    print(df[['商品コード', '倉庫在庫数']])
    
    # Assertions
    row111 = df[df['商品コード'] == '111'].iloc[0]
    assert row111['倉庫在庫数'] == 150, f"Expected 150, got {row111['倉庫在庫数']}"
    
    row222 = df[df['商品コード'] == '222'].iloc[0]
    assert row222['倉庫在庫数'] == 50, f"Expected 50, got {row222['倉庫在庫数']}"
    
    row444 = df[df['商品コード'] == '444'].iloc[0]
    assert row444['倉庫在庫数'] == 22, f"Expected 22, got {row444['倉庫在庫数']}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_calculation()
