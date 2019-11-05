#Christian Walker
#11/5/2019
#

import random

MIN = 1
MAX = 100

def main():
    print("--------------------------------------------------------------")
    print("1. Play Game")
    print("2. Exit")
    MenuC = int(input("Select 1 to play game or 2 to exit: "))
    if MenuC == 1:
        game()
    elif MenuC == 2:
        print("Exit")
    else:
        print("Enter 1 or 2")

def game():
    again = 'y'
    
    number = random.randint(MIN, MAX)
    print("--------------------------------------------------------------")
    print("A random number between 1 and 100 has been generated.")
    print("The number is", number)
    guess = int(input("Please make a guess: "))
    while again == 'y':
        if guess == number:
            print("You found the number!")
            again = 'n'
            main()
        elif guess < number:
            print("Your guess is too small :(")
            again = input("Enter 'y' to guess again: ")
            if again == 'y':
                guess = int(input("Guess: "))
            else:
                again = 'n'
                main() 
        else:
            print("Your guess is to big ;)")
            again = input("Enter 'y' to guess again: ")
            if again == 'y':
                guess = int(input("Guess: "))
            else:
                again = 'n'
                main()
main()

    
