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