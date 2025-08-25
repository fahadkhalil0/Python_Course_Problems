#Practice task no 04

#Value of a and b div by a/b if b == 0 then show a message using exception handling
try:
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = a / b

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)