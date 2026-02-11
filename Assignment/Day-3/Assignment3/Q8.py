people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

# A. Number of students
print("Number of students:", len(people))

# B. Change Lisa's favourite colour
people['Lisa'] = 'Green'

# C. Remove Jenny
people.pop('Jenny')

# D. Sort and print alphabetically
for name in sorted(people):
    print(name, ":", people[name])
