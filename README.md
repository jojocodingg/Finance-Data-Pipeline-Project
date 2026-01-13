Project Overview
This project is a personal automated ETL (Extract, Transform, Load) pipeline designed to provide data-driven investment insights. It automates the process of fetching market data, performing statistical analysis, and serving the results to a business intelligence dashboard.

The primary goal is to identify the most efficient assets by calculating the Sharpe Ratio, allowing for a clear comparison of risk-adjusted returns between high-growth equities and market benchmarks.

System Architecture
The project is built as a modular system to ensure reliability and scalability:

Data Ingestion (Data_Pipeline.py): Utilizes the Yahoo Finance API to extract time-series price data for selected tickers.

Transformation Layer (data_analysis.py): Implements SQL Window Functions (LAG, OVER, PARTITION BY) to calculate daily percentage returns directly within a relational database.

Analytics Engine (metrics.py): Employs NumPy and Pandas to calculate annualized volatility and mean returns.

Orchestration (main.py): A master script that synchronizes the execution of the entire pipeline to ensure data consistency.

Technical Stack
Language: Python 3.14 (Pandas, NumPy, YFinance)

Database: SQLite3

Visualization: Power BI

Development: VS Code, Git

Setup Instructions
Clone the repository to your local machine.

Install dependencies using the provided requirements file: pip install -r requirements.txt

Execute the pipeline by running the master script: python main.py

Visualize results by opening the Power BI file and selecting Refresh to import the latest calculated metrics.
