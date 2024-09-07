import subprocess

def run_ipynb(notebook_path):
    try:
        # Convert the notebook to a Python script using nbconvert
        
        # Run the generated Python script using subprocess
        subprocess.run(['python3', notebook_path])
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the path to your IPython Notebook file
notebook_path = '/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/SARIMAX.py'

# Call the function to run all cells of the IPython Notebook
run_ipynb(notebook_path)
