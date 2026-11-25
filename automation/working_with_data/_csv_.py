import csv
from pathlib import Path

# CSV, the language of businesses.

# contents = [
#     ["Name", "Department", "Salary",],
#     ["Alice", "Finance", "50000",],
#     ["Bob", "IT", "45000",],
#     ["John", "HR", "60000",],
# ]

# with open("employees.csv", "w", newline="") as file_obj:
#     csv_writer = csv.writer(file_obj)
#     csv_writer.writerows(contents)


# with open("employees.csv", "r",) as file_obj:
#     csv_reader = csv.reader(file_obj)  #  returns an iterator of lists
    
#     next(csv_reader)
    
#     # for row in csv_reader:
#     #     print("Name: ", row[0])
#     #     print("Department: ", row[1])
#     #     print("Salary: ", row[2])
#     #     print("-" * 25)
#     #     print("\n")


# # Read text → Convert data type → Process it → Produce output.

# with open("employees.csv") as file_obj:
#     csv_reader = csv.reader(file_obj)  
#         
#     next(csv_reader)
    
#     for row in csv_reader:
#         name, department, salary = row
#         salary = int(salary)
#         print(f"{name} earns {salary + 5000}")

with open("employees.csv") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    
    for row in csv_reader:
        name = row["Name"]
        department = row["Department"]
        salary = int(row["Salary"]) + 5000 
        
        print(f"{name} works in {department} and earns {salary}")


rows = [["Filename", "Extension"]]

for file in Path(".").iterdir():
    if file.is_file():
        rows.append([file.name, file.suffix])

with open("files.csv", "w", newline="") as file_obj:
    writer = csv.writer(file_obj)
    writer.writerows(rows)


students = [
    {
        "Name": "Taofeek",
        "Course": "Computer Science",
        "Level": 300
    },
    {
        "Name": "Ada",
        "Course": "Mathematics",
        "Level": 200
    },
    {
        "Name": "David",
        "Course": "Physics",
        "Level": 400
    }
]


with open("students.csv", "w", newline="") as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=students[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(students)



with open("students.csv") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    
    for row in csv_reader:
        name, course, level = row.values()
        print(f"{name} ({course}) - Level {level}")


# reader()
# writer()
# DictReader()
# DictWriter()
# writerow()
# writerows()
# writeheader()
# next()
# newline=""
