import subprocess

python_version = subprocess.run(["python3", "--version"], capture_output=True, text=True)  # noqa: PLW1510
print(f"Return Code: {python_version.returncode}")
print(f"Output: {python_version.stdout.strip()}")


# Your Challenge
# Write a script that:

# Prints your Python version using subprocess.
# Stores the command output in a variable instead of letting it print directly.
# Prints the exit code.
# Prints only the version string (without extra metadata).
# Finally, runs one operating system command:
# Linux: pwd or ls
# Windows: cmd /c dir