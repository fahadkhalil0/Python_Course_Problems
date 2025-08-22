with open("lorem.txt", "r") as f:
    content = f.read()

    if ("Python" in content):
        print("Python found!", content.count("Python"))
    else:
        print("Python not found.")