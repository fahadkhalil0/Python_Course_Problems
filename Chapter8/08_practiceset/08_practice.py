#Practice task no 08

#function defination
def table():
    n = int(input("Enter a number to generate multiplication table: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

#call the function here:
table()