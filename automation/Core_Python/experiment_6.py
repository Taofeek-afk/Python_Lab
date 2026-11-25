import argparse

parser = argparse.ArgumentParser(description="Back Up script")
parser.add_argument("source_folder", type=str)
parser.add_argument("destination_folder", type=str)
parser.add_argument("--zip", action="store_true")

args = parser.parse_args()

print(args.source_folder)
print(args.destination_folder)
print(args.zip)


# Build a command-line program called backup.py that accepts:

# A required source folder.
# A required destination folder.
# An optional --zip flag.

# Example usage:

# python3 backup.py Projects Backups

# or

# python3 backup.py Projects Backups --zip
