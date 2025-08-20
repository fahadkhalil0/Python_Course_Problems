# Star pattern
# like this:
#    * 
#   * *
#  * * *
# * * * *


# num = 7
# for i in range(1, num +1):
#     print(" " * (num - i) + "* " * i)

num = int(input("Enter the number of rows for the star pattern: "))

for i in range (1, num +1):
    print(" " * (num - i), end="")
    print(" " * (2 * i - 1), end="")
    print(" ")
    