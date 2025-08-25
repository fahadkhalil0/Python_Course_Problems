#Merge dictionary in python

dict1 = {
    "name" : "Fahad",
    "age" : 25,
    "dept": "BSSE"
}

dict2 = {
    "name" : "Abdul",
    "age" : 19,
    "dept": "BSAF"
}

merged = dict1 | dict2
print(merged)