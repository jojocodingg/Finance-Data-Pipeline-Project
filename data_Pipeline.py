import yfinance as yf
import sqlite3
import pandas as pd
import os

# 1. This part finds the EXACT folder where your script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'portfolio_system.db')

tickers = ['HOOD', 'META', 'GRAB', 'SPY', 'QQQ', 'AMD']

def ingest_data():
    print(f"--- Starting Ingestion ---")
    print(f"Target location: {db_path}") # This will tell us exactly where it's going
    
    try:
        # Fetching data
        raw_data = yf.download(tickers, period="3y", auto_adjust=True)['Close']
        df_long = raw_data.stack().reset_index()
        df_long.columns = ['Date', 'Ticker', 'Price']
        
        # Connect using the absolute path we created
        conn = sqlite3.connect(db_path) # the bridge to the database
        df_long.to_sql('stock_prices', conn, if_exists='replace', index=False)
        conn.close()
        
        print(f"--- SUCCESS! ---")
        print(f"File created at: {db_path}")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    ingest_data()