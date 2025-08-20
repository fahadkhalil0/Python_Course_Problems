# Factorial of a given number using for loop

num = int(input("Enter a number to find its factorial: "))
f = 1
for i in range(1, num +1): # range function in for loop is very important if you want to run it properly otherwise it will throw an error.
    f *= i
print(f"The factorial of {num} is:", f)


#Factorial using while loop
num = int(input("Enter a number to find its factorial: "))
i = 1
f = 1
while (i <= num):
    f *= i
    i += 1
#done