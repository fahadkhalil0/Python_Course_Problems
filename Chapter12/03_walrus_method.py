#Walrus Method In python
a = 10
b = 20
if (c := a + b) > 25:
    print(c)
else:
    print("No value found")

#For list
numbers = [10, 20, 30, 40, 50]
if (total := sum(numbers)) > 100:
    print(total)
else:
    print("No value found")

    