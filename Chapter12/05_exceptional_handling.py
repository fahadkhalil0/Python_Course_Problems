#Exceptional Handling In Python

try:
    n = (input("Enter the name pleaseeeee: "))
    a = int(input("Enter the age pleaseeeee: "))
    print("Your name is:", n)
    print("Your age is:", a)

except ValueError as v:
    print("Invalid input! Please enter a number.", v)

except Exception as e:
    print("An unexpected error occurred:", e)

except TypeError as te:
    print("Type error occurred:", te)
    print("End of program.")

except SyntaxError as se:
    print("Syntax error occurred:", se)

except IndentationError as ie:
    print("Indentation error occurred:", ie)

print("THe program has ended successfully!")
