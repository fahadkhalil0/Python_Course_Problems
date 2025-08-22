#Practice set no 4

word = ["Donkey", "bad", "ganda"]

with open("multiple.txt", "r") as f:
    contents = f.read()
    contentN = contents.replace("Donkey", "#" * len(word))

with open("multiple.txt", "w") as f:
    f.write(contentN)