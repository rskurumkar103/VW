list1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

frequency = {}

for num in list1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
