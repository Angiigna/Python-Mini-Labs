"""
🎯 Number Guessing Game

This Python program is an interactive number guessing game played via the terminal.
The user can select from three difficulty levels — Easy, Medium, and Hard — each
with a different range of numbers and allowed number of attempts.

Gameplay:
- The program randomly selects a number within the chosen difficulty range.
- The user has a limited number of attempts to guess the number correctly.
- After each guess, the program provides hints whether the guess is too high or too low.
- If the user guesses the number correctly, they win.
- If they use up all attempts without guessing, the correct number is revealed."""

import random  # Import the random module to generate random numbers


def start_game(level):
    # Set the range and number of attempts based on the chosen difficulty level
    if level == 1:
        # Easy: random number between 1 and 10
        random_number = random.randint(1, 10)
        attempts = 5  # 5 attempts allowed
    elif level == 2:
        # Medium: random number between 1 and 50
        random_number = random.randint(1, 50)
        attempts = 10  # 10 attempts allowed
    elif level == 3:
        # Hard: random number between 1 and 100
        random_number = random.randint(1, 100)
        attempts = 15  # 15 attempts allowed
    else:
        print("Invalid level selected.")  # Handle invalid level input
        return  # Exit the function if level is invalid

    # Loop for the number of allowed attempts
    for attempt in range(attempts):
        # Prompt user for their guess
        user_number = int(input("Guess the number: "))
        if (user_number == random_number):
            print("Congratualation! You guessed correctly ")  # Correct guess
            break  # Exit loop if guessed correctly
        elif (user_number < random_number):
            # Guess is lower than the random number
            print("Your guess is too low")
        else:
            # Guess is higher than the random number
            print("Your guess is too high")
    else:
        # This block runs if the user fails to guess correctly within allowed attempts
        print(
            f"Sorry you have exhausted all your attempts. The number was {random_number}")


def launch_game():
    print("""
      Welcome to the number guessing game!
      The game has 3 levels 
      1. Easy: You have 5 attempts to guess a number between 1 and 10
      2. Medium: You have 10 attempts to guess a number between 1 and 50
      3. Hard: You have 15 attempts to guess a number between 1 and 100
      """)  # Display game instructions and levels
    level = input(
        "Choose your level(Enter 1, 2 or 3): ")  # Ask user to choose a level
    if level == "1":
        print("You have chosen Easy level")  # Confirm level choice
        start_game(1)  # Start game with Easy level
    elif level == "2":
        print("You have chosen Medium level")  # Confirm level choice
        start_game(2)  # Start game with Medium level
    elif level == "3":
        print("You have chosen Hard level")  # Confirm level choice
        start_game(3)  # Start game with Hard level
    else:
        # Handle invalid input
        print("Invalid level. Please choose 1, 2 or 3.")


def main():
    # Main loop to allow replaying or quitting the game
    while True:
        start = input(
            # Prompt user to play or quit
            "Press enter to play or type quit to exit: ").strip().lower()
        if start == "quit":
            print("Thank you for playing")  # Exit message
            break  # Exit the loop and end the program
        elif start == "":
            launch_game()  # Start the game if user presses enter


if __name__ == "__main__":
    main()  # Run the main function if the script is executed
