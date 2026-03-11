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