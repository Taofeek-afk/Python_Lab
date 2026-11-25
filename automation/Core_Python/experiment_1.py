from pathlib import Path

# Automation_Practice/
# │
# ├── notes.txt
# ├── tasks.txt
# ├── images/
# └── backups/

# Requirements:

# Create the images and backups subfolders.
# Create empty notes.txt and tasks.txt files.

folder = {"Automation_Practice": ["notes.txt", "tasks.txt", "images", "backups"]}

for key, values in folder.items():
    path = Path(key)
    path.mkdir(exist_ok=True)
    for value in values:
        nested_path = path / value 
        if "." in value:
            nested_path.touch()
        else:
            nested_path.mkdir(exist_ok=True)


# Print every item inside Automation_Practice.
# If an item is a file, print "FILE".
# If an item is a directory, print "DIR".

for item in Path("Automation_Practice").iterdir():
    if item.is_file():
        print(f"{item.name} -> File")
    elif item.is_dir():
        print(f"{item.name} -> DIR")


# Describe, Loop, Inspect, Act
