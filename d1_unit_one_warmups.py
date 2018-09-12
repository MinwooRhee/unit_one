import turtle

turtle.speed(10)

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.forward(100)

for x in range(3):
    turtle.left(120)
    turtle.forward(100)

turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

for x in range(100):
    turtle.forward(200)
    turtle.left(120)


turtle.exitonclick()