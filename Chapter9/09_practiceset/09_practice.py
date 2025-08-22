#Practice task no 09
with open("lorem.txt", "r") as f:
    content1 = f.read()

with open("lorem_copy.txt", "r") as f:
    content2 = f.read()

if (content1 == content2):
    print("The files are identical.")
else:
    print("The files are different.")