def union(list1, list2):
    return list1 + [x for x in list2 if x not in list1]


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = union(list1, list2)
print("Union:", result)
