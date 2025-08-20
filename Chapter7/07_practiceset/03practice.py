#table of any number using while loop
num =  int(input("Generate a multiplication table of any number"))
i = 1
while(i<=10):
    print(f"{num} * {i} = ", num * i)
    i += 1