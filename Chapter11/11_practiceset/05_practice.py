#Practice task no 05
#Class of vector of n dimensions

class vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, num):
        result = vector(self.x + num.x, self.y + num.y, self.z + num.z)
        return result

    def __mul__(self, num):
        result = vector(self.x * num.x, self.y * num.y, self.z * num.z)
        return result
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    

A = vector(2,3,4)
B = vector(5,6,7)

print(A + B)
print(A * B)