tup = (1, 2, 3, 4, 2, 5, 3, 6)

value = int(input("Enter value: "))

count = tup.count(value)

if count > 1:
    print("Element is repeated", count, "times")
elif count == 1:
    print("Element exists but not repeated")
else:
    print("Element not found")
