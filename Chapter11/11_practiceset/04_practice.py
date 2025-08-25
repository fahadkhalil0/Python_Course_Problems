#Practice task no 4
class complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i


    def __add__(self, num):
        return complex(self.r + num.r, self.i + num.i)

    def __mul__(self, num):
        return complex(self.r * num.r - self.i * num.i, self.r * num.i + self.i * num.r)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = complex(2, 13)
c2 = complex(14, 5)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)