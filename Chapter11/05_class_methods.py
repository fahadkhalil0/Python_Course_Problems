# @ClassMethod in python
class Candidate:
    age = 22

    @classmethod #Class method shows the actual class atribute value
    def print(cls):
        print(f"The age is {cls.age}")

C = Candidate()
C.age = 18
C.print()