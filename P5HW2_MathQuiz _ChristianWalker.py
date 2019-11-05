#Christian Walker
#11/5/2019
#P5HW2_MathQuiz
#A program that runs 2 math games

#---------------------------Pseudcode-------------------------#
##Start menu
##-print menu options
##-if/else statement for menu choices
##--1 is additon
##--2 is subtraction
##--3 is to exit
##
##Addition game
##-generate two random numbers
##-prompt user to add the two numbers
##--get user input
##-if/else statement to decide if answer is right or wrong
##--if answer is right go back to main menu
##--else prompt user to answer again
##--loop until the answer is right
##
##Subtraction game
##-generate two random numbers
##--while statement to make sure number1 > number2
##-prompt user to subtract the two numbers
##--get user input
##-if/else statement to decide if answer is right or wrong
##--if answer is right go back to main menu
##--else prompt user to answer again
##--loop until the answer is right
#---------------------------Pseudcode-------------------------#

import random

MIN = 1
MAX = 1000

def main():
    print("--------------------------------------------------------------")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit Program")
    MenuC = int(input("Enter a function: "))
    if MenuC == 1:
        add()
    elif MenuC == 2:
        subtract()
    elif MenuC == 3:
        print("Now exiting program.")
    else:
        print("Enter 1, 2 or 3")

def add():
    again = 'y'
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    gg = number1 + number2
    print("--------------------------------------------------------------")
    print("Add these two numbers")
    print(number1, "+", number2)
    print("The sum is", gg)
    guess = int(input(""))
    while again == 'y':
        if guess == gg:
            print("You got it!")
            again = 'n'
            main()
        else:
            print("Wrong")
            again = input("Enter 'y' to guess again: ")
            if again == 'y':
                guess = int(input("Answer: "))
            else:
                main()
        
def subtract():
    again = 'y'
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)    
    while number2 > number1:
        number1 = random.randint(MIN, MAX)
        number2 = random.randint(MIN, MAX)        
    gg = number1 - number2
    print("--------------------------------------------------------------")
    print("Subtract these two numbers")
    print(number1, "-", number2)
    print("The difference is", gg)
    guess = int(input(""))
    while again == 'y':
        if guess == gg:
            print("You got it!")
            again = 'n'
            main()
        else:
            print("Wrong")
            again = input("Enter 'y' to guess again: ")
            if again == 'y':
                guess = int(input("Answer: "))
            else:
                main()
        
    

main()
