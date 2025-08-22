# copy the content of the lorem file.
with open("lorem.txt", "r") as f:
    Content = f.read()


with open("lorem_copy.txt", "w") as f:
    f.write(Content)