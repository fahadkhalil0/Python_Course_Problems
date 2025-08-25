#Operator Overloading in python

class opt:
    # a = 20
    # b = 35

    #create a consturctor
    def __init__(self, n):
        self.n = n

    def __add__(self, num):  #num is the second object
        return f"The addition of two numbers will be :: {self.n} + {num.n} is {self.n + num.n}"
    
    def __sub__(self, num):  #num is the second object
        return f"The subtraction of two numbers will be :: {self.n} - {num.n} is {self.n - num.n}"
    
    def __mul__(self, num):  #num is the second object
        return f"The multiplication of two numbers will be :: {self.n} * {num.n} is {self.n * num.n}"
    
    def __truediv__(self, num):
        return f"The turdiv of two numbers will be :: {self.n} / {num.n} is {self.n / num.n}"
    
    def __floordiv__(self, num):
        return f"The floordiv of two numbers will be :: {self.n} / {num.n} is {self.n / num.n}"
    

n = opt(50)
m = opt(10)

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)
