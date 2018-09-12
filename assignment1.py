import turtle

turtle.speed(100)

turtle.right(30)

def drawcircles():
    for x in range(200):
        turtle.circle(x)
        turtle.left(1.8)

turtle.pencolor("#ff80ff")

drawcircles()

turtle.left(120)

turtle.pencolor("#5cd6d6")

drawcircles()

turtle.left(120)

turtle.pencolor("#4d4dff")

drawcircles()

turtle.exitonclick()