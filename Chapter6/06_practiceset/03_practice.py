#practice set 03
 #it is like the spamming filter...

p1 = "Buy Now"
p2 = "Click me"
p3 = "subscribe now"
p4 = "make alot of money"

message = input("Enter the comment please")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam comment")

else :
    print("This comment is not a spam")