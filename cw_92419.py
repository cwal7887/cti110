#CW92419
#Christian Walker
#9/24/2019

#A customer at a store is purchasing five items
#Create a program that ask the user for the price of each item
#Displays subtotal of 5 items, the sales tax, and grand total
#Assume sales tax is 6%
#---------------------------Pseudcode-------------------------#
##Declare Variables
#Declare float item1
#Declare float item2
#Declare float item3
#Declare float item4
#Declare float item5
#Declare float stotal
#Declare float stax
#Declare float gtotal
##Ask user to enter price of each item
#Diplay "Enter price of item 1: $"
#Input item1
#Diplay "Enter price of item 2: $"
#Input item2
#Diplay "Enter price of item 3: $"
#Input item2
#Diplay "Enter price of item 4: $"
#Input item4
#Diplay "Enter price of item 5: $"
#Input item5
##Calculate subtotal
#stotal = item1 + item2 + item3 + item4 + item5
##Calculate sales tax
# stax = stotal * .06
##Calculate grand total
#gtotal = stotal + stax
##Display grand total
#Display "Subtotal: $" + "stotal"
#Display "Sales Tax: $" + "stax"
#Display "Grand Total: $" + "gtotal"
#-------------------------------------------------------------#
#Declare float item1
item1 = 0.0
#Declare float item2
item2 = 0.0
#Declare float item3
item3 = 0.0
#Declare float item4
item4 = 0.0
#Declare float item5
item5 = 0.0
#Declare float stotal
stotal = 0.0
#Declare float stax
stax = 0.0
#Declare float gtotal
gtotal = 0.0
##Ask user to enter price of each item
#Diplay "Enter price of item 1: $"
#Input item1
print("---------------------------------------")
item1 = float(input("Enter price of item 1: $"))
#Diplay "Enter price of item 2: $"
#Input item2
item2 = float(input("Enter price of item 2: $"))
#Diplay "Enter price of item 3: $"
#Input item3
item3 = float(input("Enter price of item 3: $"))
#Diplay "Enter price of item 4: $"
#Input item4
item4 = float(input("Enter price of item 4: $"))
#Diplay "Enter price of item 5: $"
#Input item5
item5 = float(input("Enter price of item 5: $"))
##Calculate subtotal
#stotal = item1 + item2 + item3 + item4 + item5
stotal = item1 + item2 + item3 + item4 + item5
##Calculate sales tax
# stax = stotal * .06
stax = stotal * .06
##Calculate grand total
#gtotal = stotal + stax
gtotal = stotal + stax
print("---------------------------------------")
##Display grand total
#Display "Subtotal: $" + "stotal"
print("Subtotal: $",format(stotal,',.2f') , sep='')
#Display "Sales Tax: $" + "stax"
print("Sales Tax: $",format(stax,',.2f') , sep='')
#Display "Grand Total: $" + "gtotal"
print("Total: $", format(gtotal,',.2f'), sep='')
