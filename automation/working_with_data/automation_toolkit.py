import configparser
import csv
import json
import pickle
import shutil
from datetime import UTC, datetime
from pathlib import Path

config_parser = configparser.ConfigParser()

config_parser["Backup"] = {
    "source": "documents",
    "destination": "backup",
}

config_parser["Settings"] = {
    "create_report": "True",
    "save_state": "True",
}


with open("config.ini", "w") as file_obj:
    config_parser.write(file_obj)


config_parser.read("config.ini")


source_folder = config_parser.get("Backup", "source", fallback=None)
destination_folder = config_parser.get("Backup", "destination", fallback=None)

if not source_folder or not destination_folder:
    raise KeyError("source or destination folder is missing from .ini configuration file")


source = Path(source_folder)    
destination = Path(destination_folder)


if source.is_dir():
    destination.mkdir(exist_ok=True)

    files_processed = 0
    data = []  # For CSV
    successful = False  # No file found

    for file in source.iterdir():
        if file.is_file():
            data.append({"Filename": file.name, "Size": file.stat().st_size})
            successful = True
            files_processed += 1
            # print(file.name)
            shutil.copy2(file, destination)
else:
    raise KeyError("source folder is missing")


if successful:  # Folder might be present but not have files.
    backup_state = {
        "files_processed": files_processed,
        "last_backup": datetime.now(UTC),  # Pickle preserves other data type formats.
        "successful": successful,  # True
    }
    
    metadata = {
        "backup_name": "daily_backup",
        "files": files_processed,
        "location": f"{destination}",
    }

    with open("backup.pkl", "wb") as file_obj: 
        pickle.dump(backup_state, file_obj)
    
    with open("backup_metadata.json", "w") as file_obj:
        json.dump(metadata, file_obj, indent=4)
    
    with open("backup_report.csv", "w", newline="") as file_obj:
        csv_writer = csv.DictWriter(file_obj, fieldnames=["Filename", "Size"])
        csv_writer.writeheader()
        csv_writer.writerows(data)



#  Rewrite the program to work with cmd input args.
# def load_config():
#     ...


# def find_files():
#     ...


# def copy_files():
#     ...


# def save_state():
#     ...


# def write_json():
#     ...


# def write_csv():
#     ...


# def main():
#     ...



# if __name__ == "__main__":
#     main()   ## Crucial for command line args.
