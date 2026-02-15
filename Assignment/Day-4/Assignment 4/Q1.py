def intersection(list1, list2):
    return [x for x in list1 if x in list2]


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = intersection(list1, list2)
print("Intersection:", result)
