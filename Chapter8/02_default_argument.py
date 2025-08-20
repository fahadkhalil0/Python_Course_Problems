#Default Arguments in functions
# passing the parameter/arguments of the functions
def greet(Name, msg = "Thank You"):
    # name = input("Enter the name:: ")
    print(f"Greetings {Name}!, welcome to the world of Python!")
    print(msg)

# function call
greet("Fahad")

# return value in function
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    aveg = (a+b+c)/3
    print(aveg)
    # return aveg
    print("I am out from the function")
    
avg()# calling the built-in function in the program

