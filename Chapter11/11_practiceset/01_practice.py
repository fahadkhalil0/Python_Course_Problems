#Practice task no 1

class TwoDvector:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The twoDvector is {self.i}i and {self.j}j")



class ThreeDvector(TwoDvector):

    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show3(self):
        print(f"The twoDvector is {self.i}i, {self.j}j and {self.k}k ")

twoD = TwoDvector(2,3)
twoD.show()
twoD = ThreeDvector(2,3,5)
twoD.show3()
