# Secret Santa Game - Python

## Description
This Python-based project automates the assignment of Secret Santa pairs among employees in a company. It reads employee data from a provided file, assigns pairs ensuring no one is assigned to themselves, and prevents repeating previous year’s assignments (if applicable). The result is saved to an output file (CSV or Excel).

## Requirements
- **Python 3.x**
- `pandas` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Codeproject0/assesment
    cd ashwin
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
2. **Running script**
    ```bash
    py script.py
    ```
## Input
- **Employee Data**: A CSV or Excel file (Employee-List.csv or Employee-List.xlsx) containing employee information with columns:-
- **Previous Year Data**: if available, a CSV or Excel file (Secret-Santa-Game-Result-2023.csv or Secret-Santa-Game-Result-2023.xlsx) with past Secret Santa assignments to prevent repeat pairings, filename should ends with previous year otherwise not considered.

## Ouput
- **Employee Data with gift receivers**: A Excel file with named output.xlsx