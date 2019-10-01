#Christian Walker
#10/1/2019
#P3HW2 - Meal, Tip and Tax Calculator

#---------------------------Pseudcode-------------------------#
##Ask user the price of the meal
#Display Enter price of meal
#Input meal
##Ask user would they like to tip 16, 18, or 20 percent
#if tip is 16 multiply meal by 0.16
#if tip is 18 multiply meal by 0.18
#if tip is 20 multiply meal by 0.2
#Display error if tip isnt 16, 18, or 20
##Calculate users selected tip and meal tax at 6 percent
#Calculate full price of the meal
##Display total cost of meal
#Display meal
#Display tipp
#Display tax
#Display The total price of your meal is, fmeal
#---------------------------Pseudcode-------------------------#

##Ask user the price of the meal
#Display Enter price of meal
#Input meal
meal = float(input("Enter price of meal: $"))
##Ask user would they like to tip 16, 18, or 20 percent
tip = int(input("Would you like to tip 16, 18, or 20 percent?: "))
#if tip is 16 multiply meal by 0.16
if tip == 16:
    tipp = meal * 0.16
#if tip is 16 multiply meal by 0.16
elif tip == 18:
    tipp = meal * 0.18
#if tip is 16 multiply meal by 0.16
elif tip == 20:
    tipp = meal * 0.2
#Display error if tip isnt 16, 18, or 20
else:
    print('Please enter 16, 18, or 20')
##Calculate users selected tip and meal tax at 6 percent
tax = meal * 0.06
#Calculate full price of the meal
fmeal = meal + tipp + tax
##Display total cost of meal
#Display meal
print("Meal: $", meal)
#Display tipp
print("Tip: $", tipp)
#Display tax
print("Tax: $", tax)
#Display The total price of your meal is, fmeal
print("The total price of your meal is $", fmeal)
