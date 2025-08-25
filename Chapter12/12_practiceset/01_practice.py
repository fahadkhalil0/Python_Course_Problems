#Practice task no 01
try:
    with open("file1.txt") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file1.txt not found")

except Exception as e:
    print(e)

try:
    with open("file2.txt") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file2.txt not found")
except Exception as e:
    print(e)

try:
    with open("file3.txt") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file3.txt not found")

except Exception as e:
    print(e)