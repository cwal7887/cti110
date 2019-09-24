#P2HW2 - Turtle Graphic
#Christian Walker
#9/24/2019

#A turtle program that draws five overlapping rings

#---------------------------Pseudcode-------------------------#
##Import turtle
#show the turle on screen
##Draw first circle
##Draw second circle
#Pick up pen
#Move turtle
#Drop pen
#Draw circle
##Draw second circle
#Pick up pen
#Move turtle
#Drop pen
#Draw circle
##Draw third circle
#Pick up pen
#Move turtle
#Drop pen
#Draw circle
##Draw fourth circle
#Pick up pen
#Move turtle
#Drop pen
#Draw circle
##Draw fifth circle
#Pick up pen
#Move turtle
#Drop pen
#Draw circle
#-------------------------------------------------------------#

##Import turtle
import turtle as t
t.showturtle()
##Draw first circle
t.circle(45)
##Draw second circle
t.penup()
t.goto(120,0)
t.pendown()
t.color("red")
t.circle(45)
##Draw third circle
t.penup()
t.goto(-120,0)
t.pendown()
t.color("blue")
t.circle(45)
##Draw fourth circle
t.penup()
t.goto(-60,-50)
t.pendown()
t.color("yellow")
t.circle(45)
##Draw fifth circle
t.penup()
t.goto(60,-50)
t.pendown()
t.color("green")
t.circle(45)
