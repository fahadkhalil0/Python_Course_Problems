# FInd the prime number using for loop and while loop

num = int(input("Enter a number to check if it is prime: "))

for p in range(2, num):
    if num % p == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")