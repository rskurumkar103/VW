import random
import string

characters = string.ascii_letters + string.digits
captcha = "".join(random.choice(characters) for _ in range(6))

print("CAPTCHA:", captcha)

user_input = input("Retype the CAPTCHA exactly as shown: ")

if user_input == captcha:
    print("Verification successful!")
else:
    print("Incorrect CAPTCHA. Please try again.")
