import sqlite3
import pandas as pd
import os

# Finding our database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'portfolio_system.db')

def calculate_returns():
    conn = sqlite3.connect(db_path)
    
    # 1. LAG(Price) looks at the row ABOVE (yesterday's price).
    # 2. PARTITION BY Ticker ensures we don't accidentally compare Apple today to Tesla yesterday.
    # 3. ORDER BY Date makes sure we are looking at the correct sequence of time.
    
    query = """
    SELECT 
        Date, 
        Ticker, 
        Price,
        LAG(Price) OVER (PARTITION BY Ticker ORDER BY Date) as Yesterday_Price,
        ((Price - LAG(Price) OVER (PARTITION BY Ticker ORDER BY Date)) / 
         LAG(Price) OVER (PARTITION BY Ticker ORDER BY Date)) * 100 as Daily_Return_Pct
    FROM stock_prices
    """
    
    # Pull the results into a DataFrame
    df_returns = pd.read_sql(query, conn)
    
    # Save this into a NEW table called 'stock_returns'
    df_returns.to_sql('stock_returns', conn, if_exists='replace', index=False)
    
    print("--- Day 2 Success: Silver Layer Created ---")
    print(df_returns.dropna().head(10)) # Showing the first 10 successful calculations
    
    conn.close()

if __name__ == "__main__":
    calculate_returns()