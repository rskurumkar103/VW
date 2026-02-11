lst = [10, 20, 30, (40, 50), 60]

count = 0

for item in lst:
    if type(item) == tuple:
        break
    count += 1

print("Count =", count)
