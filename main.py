# import turtle as t, Screen
# tim = t.Turtle()
# tim.forward(10)
# tim.penup()
# tim.forward(10)



# Screen =Screen()
# Screen.exitonclick()
from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.speed(1)
for i in range(15):      
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()




Screen =Screen()
Screen.exitonclick()
