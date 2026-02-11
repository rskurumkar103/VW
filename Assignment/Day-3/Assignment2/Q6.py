lst = list(map(int, input("Enter numbers separated by space: ").split()))

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest number is:", largest)
