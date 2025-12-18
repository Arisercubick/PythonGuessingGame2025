
from handlers.handlers import *
from handlers.levels import *
from handlers.score import *

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
        [maxGuesses, difficultySelected, difficultyO] = difficultySelection(
            difficulty)
    while continueOn:
        score = game(maxGuesses, difficultyO)
        again = input("Do you want to play again? (y/n): ")
        if again.lower() != 'y':
            continueOn = False
            print(f"Thanks for playing, {name}\nYour final score is {score}!")


def game(maxGuesses, difficulty):
    waitPrint("Starting the game...\n")
    levelcount = 1
    gameOver = False
    score = 0
    guessesUsed = 0
    waitPrint(
        f"You have selected difficulty level {difficulty} with {maxGuesses} maximum guesses per level.\n")
    while levelcount <= totalLevels() and not gameOver:
        levelKey = 'level' + str(levelcount)
        levelData = levelSelect(levelKey)
        waitPrint(f"Welcome to Level {levelcount}\n")
        [guessesUsed, gameOver] = playLevel(levelData, maxGuesses)
        score += scoreCal(guessesUsed)
        waitPrint(f"Your score is: {score}\n")
        if not gameOver:
            levelcount += 1
    return score


def playLevel(levelData, maxGuesses):
    guessesUsed = 1
    levelComplete = False
    while not levelComplete:
        waitPrintArray(f"Options: {levelData['array']}\n")
        waitPrint(levelData['question'])
        print("\n\n")
        answer = input("Answer: ")
        answer = answer.lower()
        if answer == levelData['answer'].lower():
            levelComplete = True
            return [guessesUsed, False]
        elif guessesUsed == maxGuesses:
            levelComplete = True
            return [guessesUsed, True]
        else:
            guessesUsed += 1
            waitPrint(f"Try again! Attempt {guessesUsed}\n")


main()
