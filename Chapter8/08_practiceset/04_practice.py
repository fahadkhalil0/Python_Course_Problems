# recursion function to perform the sum of n natural numbers

n = int(input("Enter a number to find the sum of n natural numbers: "))

def sum_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural_numbers(n-1)

print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers(n)}")