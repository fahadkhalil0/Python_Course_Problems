with open("lorem.txt", "r") as f:
    Line = f.readlines()

lineNo = 1
for line in Line:
    if ("Python" in line):
        print(f"yes python is present in Line No {lineNo}")
        break
    lineNo += 1
else:
    print("Python not found.")