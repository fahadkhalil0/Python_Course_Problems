a = int(input("Enter a number: "))
if a < 0:
    raise ValueError("Negative values are not allowed.")
else:
    print(f"You entered: {a}")


#One more program for understanding
b = int(input("Enter another number: "))
if b > 100:
    raise ValueError("Values greater than 100 are not allowed.")
else:
    print(f"You entered: {b}")

# We can also raise our exception during the program in our python program

c = int(input("Enter a third number: "))
if c == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    print(f"You entered: {c}")
