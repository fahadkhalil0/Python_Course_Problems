#practice task no 06

# Function to convert inches into cms
def coverter(n):
#formula
    r =  n * 2.54
    print(f"{n} inches is equal to {round(r, 2)} cms")

#call the function
coverter(10)