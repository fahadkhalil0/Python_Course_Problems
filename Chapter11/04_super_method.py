#Super Method in Python
class Student:
    name = "fahad"
    age = 21
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student2(Student):
    name = "Sami"
    age = 22
    University = "UET"
    dept = "BSAF"

    def showInfo(self):
        super().display() #Super decorator in python used to call the parent class property.
        print(f"University: {self.University}")
        print(f"Department: {self.dept}")

Std1 = Student2()
Std1.showInfo()

