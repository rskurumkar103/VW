import random

secret_number = random.randint(1, 100)
attempts = 7

print("Guess a number between 1 and 100")
print(f"You have {attempts} attempts.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try a smaller number.")
    elif guess < secret_number:
        print("Too low! Try a larger number.")
    else:
        print("Congratulations! You guessed the number correctly!")
        break

    attempts -= 1
    print(f"Remaining attempts: {attempts}\n")

if attempts == 0:
    print(f"Game Over! The correct number was {secret_number}.")
