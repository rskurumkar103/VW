import mod1

print("Pick one choice:")
print("1.Odd \n 2.Even \n 3.All")

choice = int(input("Enter a choice:"))
if choice == 1:
    mod1.print_odd()

elif choice == 2:
    mod1.print_even()

elif choice == 3:
    mod1.print_all()

else:
    print("Invalid choice")            