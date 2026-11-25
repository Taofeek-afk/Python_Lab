# from pathlib import Path

# n = iter([x for x in range(5, 11)])


# for x in range(5, 11):
#     path = Path(f"experiment_{next(n)}.py")
#     if not path.exists():
#         path.touch()


# files_to_clean = [Path(f"experiment_{x}.py") for x in range(5, 11)]

# for path in files_to_clean:
#     if path.exists():
#         path.unlink()
#         print(f"Removed {path.name} successfully")
