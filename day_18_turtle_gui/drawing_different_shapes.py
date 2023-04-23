import random
from turtle import Turtle, Screen
colours=["cornflowerblue", "indianred", "deepskyblue", "wheat", "orange", "green", "purple"]
t = Turtle()
t.speed(1)
t.shape("turtle")
t.color("orange")

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
   
        t.forward(100)
        t.right(angle)

for b in range(3, 11):
    t.color(random.choice(colours))
    draw_shape(b)


Screen =Screen()
Screen.exitonclick()
