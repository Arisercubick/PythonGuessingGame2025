from score import *

name = ""
maxGuesses = 0


def main():
    name = input("Enter your name: ")
    print(f"Welcome, {name}, to the Guessing Game!")
    difficultySelected = False
    while difficultySelected is False:
        difficultySelected = True
        difficulty = input(
            "please select a difficulty level (e for easy, m for medium, h for hard): ")
        difficulty = difficulty.lower()

        if difficulty == 'e':
            diff = 1
            maxGuesses = 10
        elif difficulty == 'm':
            diff = 2
            maxGuesses = 7
        elif difficulty == 'h':
            diff = 3
            maxGuesses = 5
        else:
            difficultySelected = False
            print("Invalid input, please try again.")
