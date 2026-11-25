import csv

rows = [
    {"Name": "Alice", "Department": "finance", "Salary": "50000"},
    {"Name": "Bob", "Department": "IT", "Salary": "45000"},
    {"Name": "John", "Department": "HR", "Salary": "60000"},
    {"Name": "Mike", "Department": "IT", "Salary": "55000"},
    {"Name": "Sarah", "Department": "Finance", "Salary": "70000"},
    {"Name": "David", "Department": "HR", "Salary": "40000"}, 
]


with open("employees.csv", "w", newline="") as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=["Name", "Department", "Salary"])
    csv_writer.writeheader()
    csv_writer.writerows(rows)
    
    
with open("employees.csv") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    
    Employees_Processed = 0
    Total_Payroll = 0
    Highest_Salary = 0
    Lowest_Salary = 0   # Next time use None
    Highest_Paid_Employee = ""
    Lowest_Paid_Employee = ""
    
    for index, row in enumerate(csv_reader, start=1):
        Employees_Processed += 1
        Total_Payroll += int(row["Salary"])
        
        Highest_Paid_Employee, Highest_Salary = (row["Name"], int(row["Salary"])) if int(row["Salary"]) > Highest_Salary else (Highest_Paid_Employee, Highest_Salary)
        Lowest_Paid_Employee, Lowest_Salary = (row["Name"], int(row["Salary"])) if index == 1 or int(row["Salary"]) < Lowest_Salary else (Lowest_Paid_Employee, Lowest_Salary)


    print("Payroll Summary")
    print("=" * 24)
    print(f"Employees processed: {Employees_Processed}", end="\n")
    print(f"Total Payroll: ${Total_Payroll}")
    print(f"Average Salary: ${round(Total_Payroll/Employees_Processed, 2)}")
    print("Highest Salary", ("-" * 12), f"{Highest_Paid_Employee} ({Highest_Salary})", sep="\n")
    print("Lowest Salary", ("-" * 12), f"{Lowest_Paid_Employee} ({Lowest_Salary})", sep="\n")


# Class Work

# Create this employees.csv:

# Name,Department,Salary
# Alice,Finance,50000
# Bob,IT,45000
# John,HR,60000
# Mike,IT,55000
# Sarah,Finance,70000
# David,HR,40000

# Then write a program that calculates:

# Total payroll
# Employee count
# Average salary
# Highest-paid employee
# Lowest-paid employee
# Rules
# Use csv.DictReader().
# Do not create another list to store salaries.
# Process the file one row at a time.
# Convert salaries to integers.



# Correction

# highest_salary = 0
# lowest_salary = None

# for row in csv_reader:

#     name = row["Name"]
#     salary = int(row["Salary"])

#     total_payroll += salary
#     employees_processed += 1

#     if salary > highest_salary:
#         highest_salary = salary
#         highest_paid_employee = name

#     if lowest_salary is None or salary < lowest_salary:
#         lowest_salary = salary
#         lowest_paid_employee = name