#Christian Walker
#10/1/2019
#cw10119
#Age classifier page 124

#---------------------------Pseudcode-------------------------#
#ask the user to input there age
#if the users age is less or equal to 1 display you are an infant
#if the users age is greater than 1 and less than 13 display
#you are a child
#if the users age is greater than 13 and less than 20 display
#you are a teenager
#if the number does no fit in any category display you are an adult
#---------------------------Pseudcode-------------------------#


#ask the user to input there age
age = float(input("Enter your age: "))
#if the users age is less or equal to 1 display you are an infant
if age <= 1:
    print("You are an infant.")
#if the users age is greater than 1 and less than 13 display
#you are a child
elif age > 1 and age < 13:
    print("You are a child.")
#if the users age is greater than 13 and less than 20 display
#you are a teenager 
elif age > 13 and age < 20:
    print("You are a teenager.")
#if the number does no fit in any category display you are an adult
else:
    print("You are an adult")

