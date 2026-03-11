lst = ['a', 'b', 'c', 'd', 'e']

index = lst.index('b')
lst[index:index+1] = [1, 2, 3]

print("Updated list:", lst)
