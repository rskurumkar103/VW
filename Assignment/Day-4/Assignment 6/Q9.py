def even_position(text):
    return text[1::2]

def odd_position(text):
    return text[0::2]

def string_length(text):
    return len(text)

def add_a(text):
    return text + "a" * len(text)

text = input("Enter a string: ")

print("A. Display characters from even position")
print("B. Display characters from odd position")
print("C. Display length of string")
print("D. Add 'a' at end length times")

choice = input("Choose option: ").upper()

if choice == "A":
    print(even_position(text))
elif choice == "B":
    print(odd_position(text))
elif choice == "C":
    print(string_length(text))
elif choice == "D":
    print(add_a(text))
else:
    print("Invalid choice")
