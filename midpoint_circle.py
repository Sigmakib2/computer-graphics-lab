import turtle

def plot8(cx, cy, x, y):
    for dx, dy in [( x, y),( y, x),(-x, y),(-y, x),
                   (-x,-y),(-y,-x),( x,-y),( y,-x)]:
        turtle.goto(cx+dx, cy+dy)
        turtle.dot()

def midpoint_circle(cx, cy, r):
    x, y = 0, r
    d = 1 - r

    turtle.penup()
    plot8(cx, cy, x, y)
    turtle.pendown()
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot8(cx, cy, x, y)

turtle.speed(0)
midpoint_circle(0, 0, 60)
turtle.done()
