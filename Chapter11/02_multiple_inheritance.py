#Multiple Inheritance in Python

class VC:
    company = "Tech World"
    def getInfo(self):
        self.name = input("Enter the Name: ")
        self.designation = input("Enter your designation: ")
        self.salary = input("Enter your salary: ")
        self.address = input("Enter your address: ")

    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")

#Class no 2
class head:
    def headInfo(self):
        self.head_name = "John Doe"
        self.head_designation = "Head of Department"
        self.head_salary = 5000
        self.head_address = "123 Main St"

    def displayheadInfo(self):
        print(f"Head Name: {self.head_name}")
        print(f"Head Designation: {self.head_designation}")
        print(f"Head Salary: {self.head_salary}")
        print(f"Head Address: {self.head_address}")

#class 03
class Employee(VC, head):
        tot_emp = 200
        employe_salary = 2500
        employe_dress = "Blue"
        #print all the details
        print(f"Total Employees: {tot_emp}")
        print(f"Employee Salary: {employe_salary}")
        print(f"Employee Dress: {employe_dress}")



#making an object of VC parent class.
Vc = VC()
Vc.getInfo()
Vc.displayInfo()

#Calling the parent class functions
E = Employee()
E.getInfo()
E.headInfo()
#Display the details of Multiple inherited classes
E.displayInfo()
E.displayheadInfo()
print(f"Total Employees: {E.tot_emp}")
print(f"Employee Salary: {E.employe_salary}")
print(f"Employee Dress: {E.employe_dress}")
