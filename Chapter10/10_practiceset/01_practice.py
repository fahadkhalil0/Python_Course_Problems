#Practice Task no 01
#create class that contain the info of few programmer

class programmer:
    #using dunder method.
    def __init__(self, name, age, lang, exp):
        self.name = name
        self.age = age
        self.lang = lang
        self.exp = exp

    def GetInfo(self):
        print(f"The name of programmer is {self.name},\n his age is {self.age},\n he knows {self.lang} language,\n and he has an experience of {self.exp} years.")

Dev1 = programmer("Ali", 18, "Java", 2)
Dev2 = programmer("Qareem", 15, "SQL", 1)
Dev3 = programmer("Qabool", 22, "Python", 0)
Dev4 = programmer("Ahmed", 35, "AI", 4)

Dev1.GetInfo()
Dev2.GetInfo()
Dev3.GetInfo()
Dev4.GetInfo()
