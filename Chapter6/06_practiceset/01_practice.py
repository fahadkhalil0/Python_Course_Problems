#practice task no 1
#asking the user to input the values one by one

Num1 = int(input("Enter a number ::"))

Num2 = int(input("Enter a number ::"))

Num3 = int(input("Enter a number ::"))

Num4 = int(input("Enter a number ::"))


if (Num1 > Num2 and Num1>Num3 and Num1>Num4):
    print("The largest number is :", Num1)

elif (Num2>Num1 and Num2>Num3 and Num2>Num4):
    print("The largest number is :", Num2)

elif (Num3>Num2 and Num3>Num2 and Num3>Num4):
    print("The largest number is :", Num3)

elif (Num4>Num1 and Num4>Num2 and Num4>Num3):
    print("The largest number is :", Num4)

else:
    print("All numbers are equal")

print ("The program is closed")