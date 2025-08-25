#There are several types of errors in Python
#1. SyntaxError
#2. TypeError
#3. ValueError
#4. IndexError
#5. KeyError
#6. ZeroDivisionError
#7. FileNotFoundError
#8. ImportError

#Let us try some of them


#Else with try method
try:
    num = int(input("Enter a number: "))

except ValueError as ve:
      print(f"Error: {ve}")
else:
        print(f"You entered: {num}")

#Try with the if condition including the else:
try:
    num = int(input("Enter a number: "))
    if (num == 0):
        print("Zero is not allowed.")

except ValueError as ve:
    print(f"Error: {ve}")

else:
    print(f"You entered: {num}")

#Finally with try method
try:
    num = int(input("Enter a number: "))

except ValueError as ve:
      print(f"Error: {ve}")
else:
        print(f"You entered: {num}")
finally:
    print("Execution completed.")