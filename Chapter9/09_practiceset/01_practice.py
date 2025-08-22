#Practice task no 1

File = open("poem.txt")
Content = File.read()

print("Content of the file:", Content, Content.find("twinkle"))
File.close()

