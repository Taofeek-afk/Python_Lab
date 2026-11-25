from pathlib import Path
import shutil


# Office/
# │
# ├── reports/
# │   ├── report1.txt
# │   └── report2.txt
# │
# └── backups/

folder_structure = {"office": [{"reports": ["report1.txt", "report2.txt"]}, "backups"]}

for key, values in folder_structure.items():
    path = Path(key)
    path.mkdir(exist_ok=True)
    for value in values:
        if isinstance(value, dict):
            for k, v in value.items():
                nested_path = path / k
                nested_path.mkdir(exist_ok=True)
                for item in v:
                    file = nested_path / item
                    if "." in item:
                        file.touch()
                    else:
                        file.mkdir(exist_ok=True)
                    continue
        elif isinstance(value, str):
            nested_path = path / value
            if "." in value:
                nested_path.touch()
            else:
                nested_path.mkdir(exist_ok=True)


# Uses pathlib to create the folders and files.  ✅
dest = "./office/reports"
src = "./office/backups"

shutil.copytree(dest, src, dirs_exist_ok=True)

for item in Path(src).iterdir():
    if item.is_file():
        print(f"{item.name} -> {item.stat().st_size} bytes")

# Uses shutil.copy() to copy both reports into backups. 
# Prints every file inside backups.
# Prints the size (in bytes) of each copied file using Path.stat().st_size.

# Example output:

# report1.txt -> 0 bytes
# report2.txt -> 0 bytes


# from pathlib import Path

# def create_structure(base_path: Path, structure):
#     # Case 1: It's a string (It's a file if it has an extension, otherwise a folder)
#     if isinstance(structure, str):
#         target = base_path / structure
#         if "." in structure:
#             target.touch()
#         else:
#             target.mkdir(exist_ok=True, parents=True)
            
#     # Case 2: It's a list (Loop through and recursively process each element)
#     elif isinstance(structure, list):
#         for item in structure:
#             create_structure(base_path, item)
            
#     # Case 3: It's a dictionary (The key is a folder; value contains its nested contents)
#     elif isinstance(structure, dict):
#         for folder_name, contents in structure.items():
#             new_dir = base_path / folder_name
#             new_dir.mkdir(exist_ok=True, parents=True)
#             # Recursively pass the nested contents into the folder we just made
#             create_structure(new_dir, contents)
