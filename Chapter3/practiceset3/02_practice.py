letter = ''' Dear Name,
You are selected in Dept!
Date'''

Name = input(" Enter your full name::")
Dept = input(" Enter your dept::")
Date = input(" Enter your selection date::")

letter = letter.replace('Name', Name)
letter = letter.replace('Dept',Dept )
letter = letter.replace('Date', Date)

print(letter)