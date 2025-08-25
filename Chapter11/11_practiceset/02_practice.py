#Practice task no 2

class Animal:
    def speak(self):
        print("The animal speaks")


class pet(Animal):
    def __init__(self, name, legs, eyes):
        self.name = name
        self.legs = legs
        self.eyes = eyes

    def info(self):
        print(f"Name: {self.name}, Legs: {self.legs}, Eyes: {self.eyes}")

class dog(pet):
    name = "dog"
    legs = 4
    eyes = 2
    # super().info()
    
    @staticmethod
    def bark():
        print("The dog barks")


P = pet("doggi", 4, 2)
P.info()

D = dog("dog", 4, 2)
D.info()
D.bark()