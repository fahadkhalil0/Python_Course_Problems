#Practice task no 11
with open("lorem.txt", "r") as f:
    content1 = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content1)