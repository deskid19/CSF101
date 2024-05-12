import random
secret_number = random.randint(1,10)
max_attempts = 3

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number.")

def guess_recursive(attempts_left):
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
    else:
        print(f"Wrong guess. You have {attempts_left-1} attempts left.")
        if attempts_left > 1:
            guess_recursive(attempts_left-1)
        else:
            print(f"Sorry, you could not guess the number. The correct number was {secret_number}.")
welcome_message()
guess_recursive(max_attempts)

print(f"Memory address of Secret Number {secret_number} is: {id(secret_number)}")

while True:
    try_again = input("Do you want to try again? ").lower()
    if try_again == "yes":
        guess_recursive(max_attempts)
    else:
        print("Game over")
        break