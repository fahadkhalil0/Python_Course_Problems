#List comprehension 

#make a table

n = int(input("Enter the number to make a table: "))

table = [n*i for i in range(1,11)]
print(table)