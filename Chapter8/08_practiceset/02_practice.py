# practice task no 2

# Make a function which converts celsuis to farhenheit
# function defination
def CTF():
    C = int(input("Enter the temp in celsius :: "))
    F = (C * 9/5) + 32
    print(f"{round(F, 2)}°F")

#Call the function here:-
CTF()


# function defination
def FTC():
    F = int(input("Enter the temp in Farhenheit :: "))
    C = 5* (F - 32)/9
    print(f"{round(C, 2)}°C")
    
#Call the function here:-
FTC()
