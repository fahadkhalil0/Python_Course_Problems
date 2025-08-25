# Global VS Local Variable/keyword
a = 10 #global variable

def func():
    global a
    print(a)

func()
a = 50 #Local variable
print(a)