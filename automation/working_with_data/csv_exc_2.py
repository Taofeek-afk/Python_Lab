import csv


class Department:
    total_employees_system = 0
    total_salaries_system = 0
    all_departments = {} # Maps department names to their object instances  # noqa: RUF012

    def __init__(self, name):
        self.name = name
        self.employee_count = 0
        self.total_payroll = 0

    def add_employee_metrics(self, salary):
        self.employee_count += 1
        self.total_payroll += salary
        
        Department.total_employees_system += 1
        Department.total_salaries_system += 1
        
    @property
    def average_salary(self):
        if self.employee_count == 0:
            return 0
        return self.total_payroll // self.employee_count


class Employee:
    def __init__(self, name, department_name, salary):
        self.name = name
        self.salary = int(salary)
        
        if department_name not in Department.all_departments:
            Department.all_departments[department_name] = Department(department_name)
            
        self.department = Department.all_departments[department_name]
        

        self.department.add_employee_metrics(self.salary)


# Practical 2 – Department Report

# Your boss now says:

# "Don't show me every employee. Summarize the payroll by department."

# Given this CSV:

# Name,Department,Salary
# Alice,Finance,50000
# Bob,IT,45000
# John,HR,60000
# Mike,IT,55000
# Sarah,Finance,70000
# David,HR,40000

# Your program should produce:



with open("employees.csv") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    
    for row in csv_reader:
        # Creating the object automatically increments all department and global counts
        Employee(
            name=row.get("Name", "Unknown"), # Handles name if present in CSV
            department_name=row["Department"],
            salary=row["Salary"]
        )

    
    for dept_name, dept_obj in Department.all_departments.items():
        print(f"# {dept_name}\n#")
        print(f"# Employees: {dept_obj.employee_count}")
        print(f"# Total Payroll: ${dept_obj.total_payroll}")
        print(f"# Average Salary: ${dept_obj.average_salary}\n")

# print("=" * 30)
# print("GLOBAL SYSTEM TOTALS:")
# print(f"Total Unique Departments: {len(Department.all_departments)}")
# print(f"Total Employees Overall: {Department.total_employees_system}")
# print(f"Total System Payroll: ${Department.total_salaries_system}")

    
    
# Department Summary

# Finance

# Employees: 2
# Total Payroll: $120000
# Average Salary: $60000

# IT

# Employees: 2
# Total Payroll: $100000
# Average Salary: $50000

# HR
#
# Employees: 2
# Total Payroll: $100000
# Average Salary: $50000
# Constraint

# You may not hard-code the department names.

# Your program must work even if tomorrow someone adds:

# Marketing
# Legal
# Security
# Engineering


# with open("employees.csv") as file_obj:
#     csv_reader = csv.DictReader(file_obj)
#     department_data = {}
    
#     for row in csv_reader:
#         dept = row["Department"]
#         salary = int(row["Salary"])
        
#         if dept not in department_data:
#             department_data[dept] = {"employees": 0, "payroll": 0}
        
#         department_data[dept]["employees"] += 1
#         department_data[dept]["payroll"] += salary
    
#     print("Department Summary\n")
    
#     for key, values in department_data.items():
#         print(
#             f"{key}\n",
#             f'Employees: {values["employees"]}',
#             f"Total Payroll: {values["payroll"]}",
#             f"Average Salary: {values["payroll"]/values["employees"]}",
#             "\n",
#             sep="\n",
#             )