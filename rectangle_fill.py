import turtle

def fill_rect(x1, y1, x2, y2, gap=10):
    y = min(y1, y2)

    turtle.penup()
    turtle.goto(x1, y)
    turtle.pendown()
    while y <= max(y1, y2):
        turtle.goto(x2, y)
        y += gap
        turtle.penup()
        turtle.goto(x1, y)
        turtle.pendown()

turtle.speed(0)
fill_rect(-100, -50, 100, 50)
turtle.done()
