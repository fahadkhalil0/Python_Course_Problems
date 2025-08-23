#Class of calculator capable of performing the advance operator.
# import math
# class calc:
#     msg = "Welcome to the Advance Calculator"
#     def __init__(self, num1, num2):
#         self.num1 = math.sqrt(num1)
#         self.num2 = math.cbrt(num2)

#     def getInfo(self):
#         print(self.msg)
#         print(f"Number 1: {self.num1}")
#         print(f"Number 2: {self.num2}")


# Calc = calc(9,12)
# Calc.getInfo()



class calc:
    msg = "Welcome to the Advance Calculator"
    def __init__(self, num1):
        self.num1 = num1

    def getInfo(self):
        print(f"The square of Number 1: {self.num1 * self.num1}")

Calc = calc(4)
Calc.getInfo()