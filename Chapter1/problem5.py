import os

# Path of the directory
path = "."

# List all contents
contents = os.listdir(path)

# Print them
print("Contents of directory:", '/')
for item in contents:
    print(item)
