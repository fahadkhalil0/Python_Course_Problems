# class with attribute

class Att:
    a = 10


Value = Att()
V = Value.a = 4
print(V)
print(Att.a) #No the class attribute will remain the same as it was!