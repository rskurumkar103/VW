def overlapping(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

print(overlapping([1, 2, 3], [5, 6, 2]))
