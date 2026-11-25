Repository structure

smart-backup-manager/
│
├── README.md
├── QUESTION.md
├── backup.py
├── config.ini
├── documents/
├── backup/
└── 

Problem Statement

You are tasked with building a simple backup automation tool in Python.

The program should use a configuration file to determine the source and destination folders instead of hard-coding paths.

Requirements

1. Read backup settings from a `config.ini` file containing:

.ini
[Backup]
source=documents
destination=backup

[Settings]
create_report=True
save_state=True


2. Validate that both the source and destination folders are provided in the configuration.

3. Ensure the source folder exists before continuing.

4. Create the destination folder if it does not already exist.

5. Copy every file from the source folder into the destination folder while preserving file metadata.

6. Count the total number of files successfully copied.

7. Generate a backup state file using `pickle` that stores:

   * number of processed files
   * timestamp of the backup
   * whether the backup completed successfully

8. Generate a JSON metadata file containing:

   * backup name
   * number of files backed up
   * backup location

9. Generate a CSV report containing one row for every copied file with the following columns:

   * Filename
   * Size (in bytes)

10. If the configuration is invalid or the source directory does not exist, raise an appropriate exception.

 Constraints

* Use `configparser` for configuration management.
* Use `pathlib` for filesystem paths.
* Use `shutil.copy2()` to preserve file metadata.
* Use `pickle` to store backup state.
* Use `json` for metadata.
* Use `csv.DictWriter` to generate the report.
* Do not hard-code source or destination paths inside the program.


Expected Output

After a successful execution, the project directory should contain:


config.ini
backup/
backup.pkl
backup_metadata.json
backup_report.csv


The CSV report should resemble:

.csv
Filename,Size
report.pdf,24567
notes.txt,832
photo.jpg,108923


The JSON metadata should resemble:

.json
{
    "backup_name": "daily_backup",
    "files": 3,
    "location": "backup"
}


The pickle file should contain the backup state for later restoration.

README.md

Your `README.md` can then simply explain:

- What the project does.
- Which Python modules were used.
- How to run it.
- Example directory structure.

---

I actually like this project enough that I'd rename it slightly to make it sound more professional:

> **Python Smart Backup Manager**

or

> **Configurable File Backup Automation Tool**
