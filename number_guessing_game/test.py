# we will build a number guessing game
# we will write tests for the game

import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100 (or type 'quit' to exit): ")
        if guess.lower() == 'quit':
            print("Thanks for playing!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the right number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    start_game()