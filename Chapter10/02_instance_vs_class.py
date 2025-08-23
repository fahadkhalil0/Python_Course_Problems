# Methods in python (OOP)
class Std:
    #class attributes/properties
    name = "Sushant"
    age = 18
    dept = "BSAF"
    gpa = 3.5

    #defining a function inside the class.

    def GetInfo(self):
        print(f"The Name of student is {self.name}\n, and age is {self.age},\n The dept of student is {self.dept},\nand the student maintained a strong gpa of {self.gpa} ")

#calling the function declared inside the class.

Student = Std()
Student.name = "ALi" # This is an instance attribute
Std.GetInfo(Student)