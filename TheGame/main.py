from score import *
from levels import *
from handlers import *

name = ""
maxGuesses = 0


def main():
    name = input("Enter your name: ")
    print(f"Welcome, {name}, to the Guessing Game!")
    difficultySelected = False
    continueOn = True
    while difficultySelected is False:
        difficultySelected = True
        difficulty = input(
            "please select a difficulty level (e for easy, m for medium, h for hard): ")
        difficulty = difficulty.lower()

        [diff, maxGuesses, difficultySelected] = difficultySelection(
            difficulty)

    while continueOn:
        game()
        again = input("Do you want to play again? (y/n): ")
        if again.lower() != 'y':
            continueOn = False
            print("Thanks for playing!")


def game():
    waitPrint("Starting the game...\n")


main()
