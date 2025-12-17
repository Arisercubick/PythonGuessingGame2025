from score import *
from levels import *
from handlers import *

name = ""


def main():
    name = input("Enter your name: ")
    print(f"Welcome, {name}, to the my mini Quiz!")
    difficultySelected = False
    continueOn = True
    while difficultySelected is False:
        difficultySelected = True
        difficulty = input(
            "please select a difficulty level (e for easy, m for medium, h for hard): ")
        difficulty = difficulty.lower()
        maxGuesses = 0
        [maxGuesses, difficultySelected] = difficultySelection(
            difficulty)
    while continueOn:
        game(maxGuesses)
        again = input("Do you want to play again? (y/n): ")
        if again.lower() != 'y':
            continueOn = False
            print("Thanks for playing!")


def game(maxGuesses):
    waitPrint("Starting the game...\n")
    levelcount = 1
    gameOver = False
    waitPrint(
        f"You have selected difficulty level {levelcount} with {maxGuesses} maximum guesses per level.\n")
    while levelcount <= totalLevels() and not gameOver:
        levelKey = 'level' + str(levelcount)
        levelData = levelSelect(levelKey)
        waitPrint(f"Welcome to Level {levelcount}\n")
        gameOver = playLevel(levelData)
        if not gameOver:
            levelcount += 1


def playLevel(levelData):
    guessesUsed = 0
    levelComplete = False
    while not levelComplete:
        waitPrintArray(f"Options: {levelData['array']}\n")
        waitPrint(levelData['question'])
        print("\n\n")
        answer = input("Answer: ")
        answer = answer.lower()


main()
