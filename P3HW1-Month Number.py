#Christian Walker
#10/3/2019
#P3HW1-Month Number
#Tells the user what month it is based
#on the input

#---------------------------Pseudcode-------------------------#
##Ask the user to input the month number
##Find month based on input
#Display error mesage if 'month' is less than 1 or greater than 12
#If 'month' is equal to 1 display "The month is January"
#If 'month' is equal to 2 display "The month is Febuary"
#If 'month' is equal to 3 display "The month is March"
#If 'month' is equal to 4 display "The month is April"
#If 'month' is equal to 5 display "The month is May"
#If 'month' is equal to 6 display "The month is June"
#If 'month' is equal to 7 display "The month is July"
#If 'month' is equal to 8 display "The month is August"
#If 'month' is equal to 9 display "The month is September"
#If 'month' is equal to 10 display "The month is October"
#If 'month' is equal to 11 display "The month is November"
#If 'month' is equal to 12 display "The month is December"
#---------------------------Pseudcode-------------------------#
##Ask the user to input the month number
month = int(input("Enter the month number: "))
##Find month based on input
#Display error mesage if 'month' is less than 1 or greater than 12
if month < 1 or month > 12:
    print("Please try again with valid month number 1 - 12")
#If 'month' is equal to 1 display "The month is January"    
elif month == 1:
    print("The month is Janurary")
#If 'month' is equal to 2 display "The month is Febuary"     
elif month == 2:
    print("The month is Febuary")
#If 'month' is equal to 3 display "The month is March"     
elif month == 3:
    print("The month is March")
#If 'month' is equal to 4 display "The month is April"     
elif month == 4:
    print("The month is April")
#If 'month' is equal to 5 display "The month is May"     
elif month == 5:
    print("The month is May")
#If 'month' is equal to 6 display "The month is June"     
elif month == 6:
    print("The month is June")
#If 'month' is equal to 7 display "The month is July"     
elif month == 7:
    print("The month is July")
#If 'month' is equal to 8 display "The month is August"    
elif month == 8:
    print("The month is August")
#If 'month' is equal to 9 display "The month is September"     
elif month == 9:
    print("The month is September")
#If 'month' is equal to 10 display "The month is October"     
elif month == 10:
    print("The month is October")
#If 'month' is equal to 11 display "The month is November"     
elif month == 11:
    print("The month is Novemebr")
#If 'month' is equal to 12 display "The month is December"     
elif month == 12:
    print("The month is December")
input("Press any key to continue...")
          
