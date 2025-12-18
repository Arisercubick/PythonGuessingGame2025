import time


def waitPrint(msg):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(0.05)


def waitPrintArray(msg):
    for item in msg:
        waitPrint(item)


def difficultySelection(diff):
    difficultySelected = True
    maxGuesses = 0
    if diff == 'e':
        diff = "easy"
        maxGuesses = 10
    elif diff == 'm':
        diff = "medium"
        maxGuesses = 5
    elif diff == 'h':
        diff = "hard"
        maxGuesses = 1
    else:
        difficultySelected = False
        print("Invalid input, please try again.")

    return [maxGuesses, difficultySelected, diff]
