#practice set no 8

#make a grade calculator

marks = int(input("Enter your marks:"))

if (marks >= 90):
    print("Grade: A")

elif (marks >= 80):
    print("Grade: B")

elif (marks >= 70):
    print("Grade: C")

elif (marks >= 60):
    print("Grade: D")

else:
    print("Grade: F")

print("Thank You for using the calculator and your total marks is :: ", marks)