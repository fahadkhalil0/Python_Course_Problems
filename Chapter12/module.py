def function():
    print("This is a function inside module.py")


if __name__ == "__main__":
        print("Module.py is being run directly")
        print(__name__)
        function()

