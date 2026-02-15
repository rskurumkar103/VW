def subtract(list1, list2):
    return [x for x in list1 if x not in list2]


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = subtract(list1, list2)
print("Difference (list1 - list2):", result)
