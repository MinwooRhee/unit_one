import turtle

def draw_hexagon():
    for x in range(6):
        turtle.forward(100)
        turtle.right(60)

for y in range(3):
    draw_hexagon()
    turtle.left(20)

turtle.exitonclick()