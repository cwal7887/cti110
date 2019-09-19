#Christian Walker
#9/12/2019
#Meal, Tip, and Tax Calculator
#A program that calculates the total amount
#of a meal purchased at a restaurant

#Intro
print("Hello!, Welcome to the Meal, Tip, and Tax Calculator")
print("All percentages should be entered in the following format: '.xx'")
print("---------------------------------------------------------------------")

#Ask user to enter the charge for food
meal = float(input("Enter price of the meal: $"))

#Ask user to enter the tip for server
tipP = float(input("Enter tip percentage for the server: "))

#Ask user to enter the Tax amount
taxP = float(input("Enter tax percentage: "))

#Calculate tip and tax
tip = meal * tipP
tax = meal * taxP

#Calculate price of full meal
Fmeal = meal + tax + tip

#Display total cost of meal
print("---------------------------------------------------------------------")
print("Meal: $", meal)
print("Tip: $", tip)
print("Tax: $", tax)
print("Your total bill is: $", Fmeal)

