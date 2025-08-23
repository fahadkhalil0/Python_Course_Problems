#Constructor and static method in python

class Student:
    #class attributes/properties
    name = "Sushant"
    age = 18
    dept = "BSAF"
    gpa = 3.5

    #Constructor
    def __init__(self):
        print("This is a init constructor")

    #defining a function inside the class.
    def GetInfo(self):
        print(f"The Name of student is {self.name}\n, and age is {self.age},\n The dept of student is {self.dept},\nand the student maintained a strong gpa of {self.gpa} ")

#calling the function declared inside the class.

# Std = Student()
# Std.name = "ALi" # This is an instance attribute
# Std.GetInfo()

#Incase if you want to declare your data in as an object attributes then you can do it by the usage of Init constructor.

class Student:
    #class attributes/properties
    name = "Sushant"
    age = 18
    dept = "BSAF"
    gpa = 3.5

    #Constructor
    def __init__(self, name, age, dept, gpa):
        self.name = name
        self.age = age
        self.dept = dept
        self.gpa = gpa

    @staticmethod #static method is known as Decorator.
    def SetInfo():
        print("Getting the info of student individually.")
        
    #defining a function inside the class.
    def GetInfo(self):
        print(f"The Name of student is {self.name}\n, and age is {self.age},\n The dept of student is {self.dept},\nand the student maintained a strong gpa of {self.gpa} ")


student = Student("Ali", 20, "BSAF", 3.8)
student.SetInfo()
student.GetInfo()