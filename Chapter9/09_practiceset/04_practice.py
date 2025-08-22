#Practice set no 4

word = "Donkey"

with open("multiple.txt", "r") as f:
    contents = f.read()
    contentN = contents.replace("Donkey", "####")

with open("multiple.txt", "w") as f:
    f.write(contentN)