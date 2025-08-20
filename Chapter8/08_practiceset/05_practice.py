# star pattern using function


def pattern(n):
    if(n == 0):
        return
    else:
        print("*" * n)
        pattern(n-1)

        
#call the function 
pattern(6)