# Match Case in Python

def sum(status):
    match status:
        case 100:
            return "Ok"
        case 200:
            return "Created"
        case 300:
            return "Accepted"
        case 400:
            return "Bad Request"
        case _:
            return "Internal Server Error"

print(sum(100))
print(sum(200))
print(sum(300))
print(sum(400))
print(sum(500))
