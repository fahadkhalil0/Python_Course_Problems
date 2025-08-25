#Practice task no 07

#use the len method/operator

class vector:
    # Constructor
    def __init__(self, l):
        self.l = l

    #Other overloading method.
    def __len__(self):
        return len(self.l)
    
#Creating an object of class vector
A = vector([1,2,3,4,5,6,7,8])
print(len(A))