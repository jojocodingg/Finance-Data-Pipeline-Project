import subprocess
import sys

def run_pipeline():
    print("--- Starting Financial Engineering Pipeline  ---")
    
    scripts = [
        "Data_Pipeline.py",     # Get raw prices
        "data_analysis.py",  # Calculate daily returns (SQL)
        "metrics.py",        # Calculate Sharpe/Risk (Python/NumPy)
        "export.py"          # Save to CSV for Power BI
    ]
    
    for script in scripts:
        print(f"Executing {script}...")
        # Use sys.executable to ensure the same Python interpreter is used
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"{script} finished successfully.")
        else:
            print(f"Error in {script}:")
            print(result.stderr)
            break
            
    print("\n--- Pipeline Complete! ---")
    print("Next Step: Open Power BI and click 'Refresh'.")

if __name__ == "__main__":
    run_pipeline()