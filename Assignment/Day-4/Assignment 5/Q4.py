import random
import string


length = int(input("Enter password length (8-12 recommended): "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*"

password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(special)
]

all_chars = uppercase + lowercase + digits + special

for _ in range(length - 4):
    password.append(random.choice(all_chars))

random.shuffle(password)

final_password = "".join(password)

print("\nGenerated Password:", final_password)
