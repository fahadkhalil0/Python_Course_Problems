#practice task no 1
#print multiplication table of given number

num =  int(input("Generate a multiplication table of any number"))
for j in range(1,11):
    print(f"{num} * {j} = ", num * j)

#table of any number using while loop
i = 1
while(i<=10):
    print(f"{num} * {i} = ", num * i)
    i += 1

#with break statement
i = 1
while(i<=10):
    if (i == 7):
        break
    print(f"{num} * {i} = ", num * i)
    i += 1

#with continue statement
i = 1
while(i<=10):
    if (i == 6):
        continue
    print(f"{num} * {i} = ", num * i)
    i += 1