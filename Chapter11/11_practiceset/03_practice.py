#Practice task no 3

class Employee:
    salary = 1000
    # increment = 10

    @property
    def salaryafterincrement(self):
        return self.salary + (self.salary * self.increment / 100)
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, newSalary):
        self.increment = ((newSalary/self.salary)-1)*100

E = Employee()
E.salaryafterincrement = 3000
print(E.increment)