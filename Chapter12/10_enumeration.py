#Enumeration in python

#List definition
l = [3,4,5,6,7]
index  = 0

#Loop usage 
# for item in l:
#     print(f"The item no at index: {index} is {item}")
#     index += 1

#This can be simplified by using the enumeration.

for index, item in enumerate(l):
    print(f"The item no at index: {index} is {item}")

# Enumeration refers to the process of iterating over something while keeping track of both the index (position) and the value at the same time.