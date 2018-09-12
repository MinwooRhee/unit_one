# Minwoo Rhee
# 9/12/18
# 9/12/18 11:01 AM
# assignment1
# draws a pattern with three sets of circles growing bigger in different colors

import turtle

turtle.speed(100)

turtle.right(30)


def drawcircles():
    for x in range(200):
        turtle.circle(x)
        turtle.left(1.8)
# This is a function that draws many circles. Each time they get bigger.
# The loop is used 200 times and the circles change angles by 1.8 degrees each time.
# Since 200 x 1.8 = 360, the turtle will come back to the angle it started when the loop ends


turtle.pencolor("#ff80ff")

drawcircles()

turtle.left(120)

turtle.pencolor("#5cd6d6")

drawcircles()

turtle.left(120)

turtle.pencolor("#4d4dff")

drawcircles()

turtle.exitonclick()