#Property decorator and getter and setter in python.
class Student:

    def __init__(self,age):
        # self.name = name
        self.age = age

    @property 
    def name(self):
        return f"{self.name}"

    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]

        #both setter and the property decorator are the concepts of abstraction and Encapsulation that restrict direct access to the object's attributes.

S = Student(39)
S.name = "John Doe"
print(S.fname, S.lname)