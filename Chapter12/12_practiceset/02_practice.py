#practice task no 02

# Enumerates the list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# for i, item in enumerate(numbers):
#     if i in (2, 4, 6):
#         print(f"The number at index {i} is {item}")

# Through while loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
while i < len(numbers):
    item = numbers[i]
    if i in (2, 4, 6):
        print(f"The number at index {i} is {item}")
    i += 1
