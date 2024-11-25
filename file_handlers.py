import os
import pandas as pd
import datetime

def read_file(file_name):
    try:
        if file_name.endswith(".csv"):
            return pd.read_csv(file_name)
        elif file_name.endswith(".xlsx"):
            return pd.read_excel(file_name)
    except Exception as e:
        raise Exception(f"Error reading {file_name}: {e}")

def load_employee_data(employee_file):
    try:
        return read_file(employee_file)
    except Exception as e:
        raise Exception(f"Error reading {employee_file}: {e}")

def load_last_year_data():
    last_year = datetime.datetime.now().year - 1
    try:
        previous_year_files = os.listdir()
        _prev_yr_files = list(filter(lambda x: str(last_year) in x, previous_year_files))
        if _prev_yr_files:
            return read_file(_prev_yr_files[0])
        return
    except Exception as e:
        raise Exception(f"Error reading {previous_year_files}: {e}")
    
def export_assignments(assignments, output_file):
    assignments.to_excel(output_file, index=False)
    print(f"Assignments saved to {output_file}")