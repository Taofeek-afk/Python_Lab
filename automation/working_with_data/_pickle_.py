import pickle

# from pathlib import Path

# student = {
#     "name": "Taofeek",
#     "skills": ["Python", "Linux", "Networking"],
#     "level": 300,
#     "active": True
# }

# with open("student.pkl", "wb") as file_obj:
#     pickle.dump(student, file_obj)


# with open("student.pkl", "rb") as file_obj:
#     student = pickle.load(file_obj);


# print(student)
# print(type(student))
# print(student["name"])
# print(student["skills"][1])


# backup_folder = Path("Backups")

# with open("backup.pkl", "wb") as file_obj:
#     pickle.dump(backup_folder, file_obj)
    

# with open("backup.pkl", "rb") as file_obj:
#     path = pickle.load(file_obj)
    
# print(path)
# print(type(path))
# print(path.name)


# numbers = [10, 20, 30]

# settings = {
#     "theme": "dark",
#     "autosave": True
# }

# project_folder = Path("Projects")


# with open("data.pkl", "wb") as file_obj:
#     for x in [numbers, settings, project_folder]:
#         pickle.dump(x, file_obj)

# with open("data.pkl", "rb") as file_obj:
#     for x in [numbers, settings, project_folder]:
#         x = pickle.load(file_obj)

# print(numbers, settings, project_folder, project_folder.name)


tasks = {
    "completed": [
        "Learn JSON",
        "Learn CSV"
    ],
    "pending": [
        "Learn SQLite",
        "Learn FastAPI"
    ]
}

with open("tasks.pkl", "wb") as file_obj:
    pickle.dump(tasks, file_obj)


with open("tasks.pkl", "rb") as file_obj:
    tasks = pickle.load(file_obj)


tasks["pending"].append("Learn configparser")

with open("tasks.pkl", "wb") as file_obj:
    pickle.dump(tasks, file_obj)

with open("tasks.pkl", "rb") as file_obj:
    tasks = pickle.load(file_obj)

for key, items in tasks.items():
    print(key.capitalize()+":")
    for item in items:
        print("  ", item)
    print()
