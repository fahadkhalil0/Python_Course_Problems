#multiplication table of n number using for loop

# num = 5

num = int(input("Enter a number to print its multiplication table: "))
# for j in range(1, num +1):
#     print(f"{num} X {j} = ", num * j)

#multiplication table of n number using for loop with reversed order
for j in range(num, 0, -1):
    print(f"{num} X {j} = ", num * j)


#one more methods
for i in range(1, 11):
    print(f"{num} X {11-i} = ", num * (11-i))