#Practice task no 5
#List comprehension and store in a file by using I/O file handling
#make a table
n = int(input("Enter the number to make a table: "))

table = [n*i for i in range(1,11)]
#writing in a file a table of entered number.

with open("table.txt", "a") as f:
    f.write(str(table) + "\n")