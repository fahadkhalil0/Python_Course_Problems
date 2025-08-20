##practice set #02

#find the perchantage of three subjects

sub1 = int(input("Enter the marks of subject 1 ::"))

sub2 = int(input("Enter the marks of subject 2 ::"))

sub3 = int(input("Enter the marks of subject 3 ::"))

#total sum of three subjects

total = sub1 + sub2 + sub3
#percentage.
percentage = (total / 300) * 100

if (percentage >= 40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("You are pass")
else:
    print("You are fail")

print("The percentage is :", percentage)