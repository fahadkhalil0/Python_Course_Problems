# find the sum of first n natural number using while loop

n = int(input("Enter a number to find the sum of first n natural numbers: "))
sum = 0
i = 1
while (i<=n):
    sum += i
    i += 1 # it will increase one in i on every iteration.
print(f"The sum of first {n} natural numbers is:", sum)