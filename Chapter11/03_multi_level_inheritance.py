#Multilevel Inheritance in python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Creating objects and displaying information
person = Person("Alice", 30)
employee = Employee("Bob", 25, "E123")
manager = Manager("Charlie", 40, "M456", "HR")

print("Person Information:")
person.display_info()

print("\nEmployee Information:")
employee.display_info()

print("\nManager Information:")
manager.display_info()
