import random
import time

age = int(input("Enter your age: "))
legal = 18
numbers = [1, 2, 3, 4, 5, 6]


def authentication():
    if age >= legal:
        print("You are legal of age and therefore allowed to play")
        roll_die()
    else:
        print("You are not over 18 yet")
        return


def roll_die():
    x = int(input("Enter your guess: "))
    if x in numbers:
        temp = random.choice(numbers)
        print(temp)

    else:
        print("your number has to be between 1-6")
        roll_die():


def roll_again():
    answer = input("Would you like to play again? y OR n: ")
    if answer == "yes" or answer == "y" or answer == "ye":
        roll_die()
    else:
        return


authentication()
