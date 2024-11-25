import random
from file_handlers import export_assignments, load_employee_data, load_last_year_data

def assign_secret_santa(employees, last_year_data):
    employee_emails = employees["Employee_EmailID"].tolist()
    last_year_mapping = {}

    if last_year_data is not None:
        for _, row in last_year_data.iterrows():
            last_year_mapping[row["Employee_EmailID"]] = row["Secret_Child_EmailID"]

    shuffled_emails = employee_emails.copy()
    random.shuffle(shuffled_emails)

    assignments = {}
    available_recipients = shuffled_emails.copy()

    for giver in employee_emails:
        for receiver in available_recipients:
            if giver != receiver and receiver != last_year_mapping.get(giver):
                assignments[giver] = receiver
                available_recipients.remove(receiver)
                break

    return assignments


def save_assignments(employees, assignments, output_file):
    employees["Secret_Child_EmailID"] = employees["Employee_EmailID"].map(assignments)
    employees["Secret_Child_Name"] = employees["Secret_Child_EmailID"].map(
        employees.set_index("Employee_EmailID")["Employee_Name"].to_dict()
    )
    export_assignments(employees, output_file)

def start(employee_file, output_file):
    employees = load_employee_data(employee_file)
    last_year_data = load_last_year_data()

    if employees.empty:
        raise Exception("Employee list is empty.")
    if len(employees) < 2:
        raise Exception("Not enough employees to assign Secret Santas.")

    assignments = assign_secret_santa(employees, last_year_data)
    save_assignments(employees, assignments, output_file)


employee_file = "Employee-List.xlsx"
output_file = "output.xlsx"
start(employee_file, output_file)