import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'portfolio_system.db')

def create_risk_free_return():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM portfolio_metrics", conn)

    plt.figure(figsize=(10, 6)) # always do figure first to create the canvas

    # Create the scatter plot
    plt.scatter(df['Annual_Volatility'], df['Annual_Return'], s= 100, alpha=0.7)
    # x axis is volatility as this is the uncertainty/risk which u are willing to take more
    # y axis is the annual return as this is the output you want to achieve

    # Label each point with the ticker symbol
    # i is the index and txt is the Ticker

    for i, txt in enumerate(df['Ticker']):
        plt.annotate(
            txt,
            (df['Annual_Volatility'].iat[i], df['Annual_Return'].iat[i]),
            textcoords="offset points",
            xytext=(7,7),
            fontsize = 10,
            fontweight='bold'
        )
    

    # 2. Add titles and axis labels (Professional Polish)
    plt.title('Portfolio Risk vs. Reward Profile', fontsize=14, fontweight='bold')
    plt.xlabel('Annual Volatility (%) - "The Risk"', fontsize=12)
    plt.ylabel('Annual Return (%) - "The Reward"', fontsize=12)
    
    # 3. Add a grid so you can trace the numbers easily
    plt.grid(True, linestyle='--', alpha=0.6)

    # 4. Save and Show
    plt.tight_layout() # This prevents the labels from getting cut off
    plt.savefig(os.path.join(script_dir, 'portfolio_chart.png'))
    print("Chart saved as portfolio_chart.png")
    plt.show()

    conn.close()

if __name__ == "__main__":
    create_risk_free_return()