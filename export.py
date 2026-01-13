import sqlite3
import pandas as pd
import os

# 1. Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'portfolio_system.db')

def export_for_powerbi():
    # 2. Connect to the database
    conn = sqlite3.connect(db_path)
    
    # 3. Pull the metrics we calculated in the previous step
    # We want the table where we saved the Sharpe Ratios
    df = pd.read_sql("SELECT * FROM portfolio_metrics", conn)
    
    # 4. Final Clean 
    # Ensure Ticker is the first column and remove any weird index columns
    if 'index' in df.columns:
        df = df.drop(columns=['index'])
        
    # 5. Save the clean version for Power BI
    output_path = os.path.join(script_dir, 'powerbi_data.csv')
    df.to_csv(output_path, index=False)
    
    print(f"Success: {output_path} updated")
    print(f"--- Data includes: {df.columns.tolist()} ---")
    
    conn.close()

if __name__ == "__main__":
    export_for_powerbi()