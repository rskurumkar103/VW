# 1] Area and Perimeter of Rectangle
l, b = map(int, input("Enter the length and breadth of rectangle: ").split())
print(f"Area of rectangle is {l * b}")
print(f"Perimeter of rectangle is {2 * (l + b)}\n")


# 2] Celsius to Fahrenheit
c = float(input("Enter the temperature in Celsius: "))
print(f"The temperature in Fahrenheit is {(c * 1.8) + 32}\n")


# 3] Accept 4-digit number
num = int(input("Enter a 4-digit number: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

print("\na) Face value of digits:", d1, d2, d3, d4)

print(f"b) Place value of each digit:")
print(f"{num} = {d1*1000} + {d2*100} + {d3*10} + {d4}")

print("c) Number in reverse order:", str(num)[::-1], "\n")


# 4] Average of three numbers
n1, n2, n3 = map(int, input("Enter 3 numbers to find average: ").split())
avg = (n1 + n2 + n3) / 3
print(f"Average of numbers is {avg}\n")


# 5] Function to find maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)

print("Maximum of three numbers is:", maximum(n1, n2, n3), "\n")


# 6] Voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting.\n")
else:
    print("You are NOT eligible for voting.\n")


# 7] Check positive, negative or zero
num2 = float(input("Enter a number to check positive/negative/zero: "))
if num2 > 0:
    print("Number is Positive.\n")
elif num2 < 0:
    print("Number is Negative.\n")
else:
    print("Number is Zero.\n")


# 8] Telephone bill calculation
calls = int(input("Enter number of telephone calls: "))
bill = 200 

if calls > 100:
    extra = calls - 100
    if extra <= 50:
        bill += extra * 0.60
    else:
        bill += 50 * 0.60
        extra -= 50
        if extra <= 50:
            bill += extra * 0.50
        else:
            bill += 50 * 0.50
            extra -= 50
            bill += extra * 0.40

print(f"Total telephone bill is Rs. {bill}\n")


# 9] Leap year check
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.\n")
else:
    print(f"{year} is NOT a Leap Year.\n")


# 10] Grade based on average of 3 subjects
m1, m2, m3 = map(int, input("Enter marks of 3 subjects: ").split())
avg_marks = (m1 + m2 + m3) / 3
print("Average marks =", avg_marks)

if 90 <= avg_marks <= 100:
    print("Grade: A")
elif 80 <= avg_marks < 90:
    print("Grade: B")
elif 70 <= avg_marks < 80:
    print("Grade: C")
elif 60 <= avg_marks < 69:
    print("Grade: D")
else:
    print("Grade: F")