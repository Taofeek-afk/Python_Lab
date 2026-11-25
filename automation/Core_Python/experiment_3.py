from pathlib import Path
from datetime import datetime
import shutil
# imagine you have:

# Projects/
# │
# ├── app.py
# ├── config.json
# ├── data.csv
# └── README.md

# Write a script that:

# Creates a Backups folder if it doesn't exist.

backup_path = Path("Backups")
backup_path.mkdir(exist_ok=True)

timestamp = f"{datetime.now().strftime('%Y-m-d_H-M-S')}"
timestamped_backup_folder = backup_path / timestamp
timestamped_backup_folder.mkdir(exist_ok=True)

src = Path("Projects")

if not src.exists():
    print("Source folder does not exist.")
    raise SystemExit

if not src.exists():
    exit()

for file in src.iterdir():
    if file.is_file():
        shutil.copy(file, timestamped_backup_folder)  # Can accept file path as args
        print(f"Copied: {file.name}")
    # if file.name == src.iterdir()[-1]:


shutil.make_archive(str(timestamped_backup_folder), "zip", str(timestamped_backup_folder)) # Can't accept file_path as args

print("Backup Complete", f"Archive {timestamped_backup_folder}.zip", sep="\n")

# Copies every file from Projects into that backup folder.

# Creates a timestamped backup folder, such as:

# Backups/
#     2026-07-23_08-45-12/


# Creates a ZIP archive of the backup.

# Prints a summary, for example:

# Copied: app.py
# Copied: config.json
# Copied: data.csv
# Copied: README.md

# Backup complete!
# Archive: 2026-07-23_08-45-12.zip

# This is very close to something a system administrator or DevOps engineer might actually use.
