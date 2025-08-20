# practice task no 1

#Find the greatest number from three numbers

# def great(a,b,c): # we can also pass the arguments in our functions.

def great(): 
    a = int(input("Enter first number: "))
    b = int(input("Enter first number: "))
    c = int(input("Enter first number: "))

    if (a>b and a>c):
        print(f"{a} is the greatest number")
    elif (b>a and b>c):
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")
        print("Thank you for using this program")

#call the function
great(12,56,89)