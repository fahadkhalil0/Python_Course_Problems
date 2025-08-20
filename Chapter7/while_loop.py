# while loop in python
#While loop is used to iterate the set of statements sequentially.

#print 1 to 50

#quick quiz

# i = 0
# while (i<50):
#     print(i)
#     i +=1

# while loop with the list
i = 0
L = ["Harry", 25,78,99,100,"Python", "Programming"]
# while (i<len(L)):
#     print(L[i])
#     i += 1

# while loop with tuple

tup = ("Harry", "Code", 12,78,900)
j = 0
# while (j<len(tup)):
#     print(tup[j])
#     j = j + 1

# while loop with tuple
Set = {"Harry", "Code","Fawad", 12,78,900}
Set = list(Set)
k = 0
while (k<len(Set)):
    print(Set[k])
    k += 1 # showing an error because set is not indexed and unordered and it is immutable.

    # if you want to print with indexing in set first convert this into list then print the items