"""SS9 - Functions for Guessing Game

Defines four functions:

1. get_requirements()
2. get_lower()
3. get_upper()
4. play_game()
"""
import random


def get_requirements():
    """prints the program requirements"""
    print("\nDeveloper: Lenny Paz")
    print("Guessing Game!")
    print("\nProgram Requirements:\n"
          + "1. Create guessing game based upon pseudo-random numbers.\n"
          + "2. Must perform data and range validation.\n")

    print("***Resource(s):***\n"
          + "Generate pseudo-random numbers: https://docs.python.org/3/library/random.html\n")

    print("Input:")


def get_lower():
    """prompts for lower number with data validation, returns int"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            lower = 0

            # prompt for lower number
            lower = int(input("Enter lower number: "))

            is_within_range = False
            while not is_within_range:
                if lower >= -1000 and lower <= 1000:
                    is_within_range = True
                else:
                    print("Lower must be between -1000 and 1000.\n")
                    lower = int(input("Enter lower: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return lower


def get_upper():
    """prompts for upper number with data validation, returns int"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            upper = 0

            # prompt upper number
            upper = int(input("Enter upper number: "))

            is_within_range = False
            while not is_within_range:
                if upper >= -1000 and upper <= 1000:
                    is_within_range = True
                else:
                    print("Upper must be between -1000 and 1000.\n")
                    upper = int(input("Enter upper: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return upper


def play_game(lower, upper):
    """generates random number and runs interactive guessing game"""
    # initialize variables
    count = 0
    rand_int = random.randint(lower, upper)

    while True:
        count += 1
        guess = int(input("\nEnter guess: "))

        if guess < rand_int:
            print("Too low!")
        elif guess > rand_int:
            print("Too high!")
        else:
            print("Bingo! Number of tries:", count, "\n")
            break
