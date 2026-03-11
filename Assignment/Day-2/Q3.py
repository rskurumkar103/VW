num = int(input("Enter a 4-digit number: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

print("\na) Face value of digits:", d1, d2, d3, d4)

print(f"b) Place value of each digit:")
print(f"{num} = {d1*1000} + {d2*100} + {d3*10} + {d4}")

print("c) Number in reverse order:", str(num)[::-1], "\n")