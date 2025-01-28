I'll walk you through building a simple number guessing game in Python step by step. As we go, I'll explain the syntax used in each part so you can learn and understand how Python works.

### Step 1: Setting up the structure of the game

We’ll start by creating a basic framework for the game. The idea will be for the computer to randomly choose a number, and the player will have to guess it.

Here's the first part of the code:

```python
import random  # Importing the random module to generate random numbers

def start_game():
    print("Welcome to the Number Guessing Game!")  # Greeting message
    number_to_guess = random.randint(1, 100)  # The computer chooses a number between 1 and 100
    attempts = 0  # Keeps track of how many attempts the player has made

    while True:
        guess = input("Guess a number between 1 and 100: ")  # Asking user to input a guess
        try:
            guess = int(guess)  # Converting the input to an integer
        except ValueError:
            print("Please enter a valid number.")
            continue  # If the user enters a non-number, the game will prompt again

        attempts += 1  # Increment attempts after each guess

        if guess < number_to_guess:
            print("Too low! Try again.")  # If the guess is too low
        elif guess > number_to_guess:
            print("Too high! Try again.")  # If the guess is too high
        else:
            print(f"Congratulations! You guessed the right number {number_to_guess} in {attempts} attempts.")
            break  # Exit the loop if the player guesses correctly
```

### Explanation of the code so far:

- **`import random`**: This imports Python's built-in `random` module, which allows us to generate random numbers. You’ll be using it to randomly pick a number for the game.
- **`def start_game()`**: This defines a function named `start_game`. Functions are reusable blocks of code that can be called to execute. The game logic will be inside this function.
- **`random.randint(1, 100)`**: This generates a random integer between 1 and 100. The `randint()` function from the `random` module is what gives us the number to guess.
- **`input("...")`**: This asks the user for input. `input()` returns the input as a string, which is why we use `int()` to convert it to an integer.
- **`try...except` block**: This is error handling. If the user enters something that can’t be converted to an integer, we catch the `ValueError` and ask them to try again.

### Step 2: Adding the game loop

We’ve already included a loop (`while True:`) that allows the player to keep guessing until they get the correct number. Now let’s add an option for the player to quit the game.

```python
def start_game():
    print("Welcome to the Number Guessing Game!")  
    number_to_guess = random.randint(1, 100)  
    attempts = 0  

    while True:
        guess = input("Guess a number between 1 and 100 (or type 'quit' to exit): ")  # Added 'quit' option
        if guess.lower() == 'quit':  # Checking if the user typed 'quit'
            print("Thanks for playing!")
            break  # Exit the loop if 'quit' is entered

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
```

### Explanation of new code:

- **`if guess.lower() == 'quit':`**: The `lower()` method converts the input to lowercase, so the player can type "QUIT", "Quit", or "quit" to exit. If the input is "quit", we break out of the loop and end the game.
- **`continue`**: If the player enters an invalid value (anything that's not a number or "quit"), `continue` will skip the rest of the code in the loop and ask them to guess again.
  
### Step 3: Running the game

To make the game run, we need to call the function we created. Here's how you can do that:

```python
if __name__ == "__main__":  # This ensures the game only starts if this file is run directly
    start_game()  # Calls the function to start the game
```

### Full Code:

```python
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
```

### Explanation of the final pieces:

- **`if __name__ == "__main__":`**: This is a common Python pattern. It ensures that the `start_game()` function is only called if the script is run directly. This is useful when your Python file might be imported elsewhere (as a module).
- **Game flow**: The game will prompt the player to guess a number, provide feedback on whether the guess is too low or too high, and will stop when the player guesses correctly or types "quit".

### What you’ve learned so far:
- Functions (`def`)
- Loops (`while`)
- Conditionals (`if`, `elif`, `else`)
- Error handling (`try...except`)
- Handling user input (`input()`)
- Using modules (`import random`)
- Using `break` and `continue` to control loop flow

===========
