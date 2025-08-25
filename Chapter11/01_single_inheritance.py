# Inheritance in Python
class Manager:
    name = "Daniel"
    salary = 15000
    address = "Islamabad Capital"

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")

class Employee(Manager):
    
    def getInfo(self):
        self.name = input("Enter Name: ")
        self.dept = input("Enter Department: ")
        self.salary = input("Enter Salary: ")
        self.address = input("Enter Address: ")


class Pion(Employee):
    name = "Shahroz"
    salary = 1500

a = Manager()
a.showInfo()

b = Employee()
b.getInfo()
b.showInfo()

c = Pion()
# c.getInfo() # Here it will show the error because 'Pion' object has no attribute 'getInfo' and Pion class is using only single level inheritance.
c.showInfo()