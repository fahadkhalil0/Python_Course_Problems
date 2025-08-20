#practice set no 07
# remove a word from list and also use the strip() method/function.

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Ali", "Awais", "Sara", "Tariq", "Subhan", "an"]
print(remove(l, "an"))