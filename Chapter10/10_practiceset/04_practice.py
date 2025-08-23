#Copy problem no 2 and use the static method with greet message.

class calc:
    #Using dunder method
    @staticmethod
    def greet():
        print("Welcome to the Advance Calculator")

    def __init__(self, num1):
        self.num1 = num1

    def square(self):
        print(f"The square of Number 1: {self.num1 * self.num1}")

    def cube(self):
        print(f"The cube of Number 1: {self.num1 * self.num1 * self.num1}")

    def sqroot(self):
        print(f"The square root of Number 1: {self.num1 **1/2}")

Calc = calc(4) #Set the num
Calc.greet() #calling all the funtions one by one
Calc.square()
Calc.sqroot()
Calc.cube()