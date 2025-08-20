# Recuursion in python
# Recursion is defined as the function which calls itself in the program

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n * fact(n-1) # here i used recursion method to make my program more easy and concised.


# call the function
n = int(input("Enter a number to find the factorial "))
print(fact(n))