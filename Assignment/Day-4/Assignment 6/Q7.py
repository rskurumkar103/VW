list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)

list_str = list(map(str, list_numbers))
tuple_str = list(map(str, tuple_numbers))

print("List to strings:", list_str)
print("Tuple to strings:", tuple_str)
