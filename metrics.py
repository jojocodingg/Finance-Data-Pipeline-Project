import sqlite3
import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'portfolio_system.db')

def calculate_gold_metrics():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM stock_returns", conn)
    
    # --- THE BRUTE FORCE  ---
    # 1. Strip hidden spaces from all column names
    df.columns = df.columns.str.strip()
    
    # 2. Automatically find the return column even if the name is slightly off
    # It looks for any column containing 'Return' or 'Pct'
    return_col = [c for c in df.columns if 'Return' in c or 'Pct' in c][0]
    print(f"Found return column: '{return_col}'")
    
    # 3. Perform the Math
    metrics = df.groupby('Ticker')[return_col].agg(['mean', 'std']).copy()
    
    # Annualizing 
    metrics['Annual_Return'] = metrics['mean'] * 252
    metrics['Annual_Volatility'] = metrics['std'] * np.sqrt(252)
    metrics['Sharpe_Ratio'] = metrics['Annual_Return'] / metrics['Annual_Volatility']
    
    print("\n--- Day 3 Success: Performance Metrics ---")
    print(metrics[['Annual_Return', 'Annual_Volatility', 'Sharpe_Ratio']])
    
    # Save to Gold Table
    metrics.to_sql('portfolio_metrics', conn, if_exists='replace')
    conn.close()

if __name__ == "__main__":
    calculate_gold_metrics()