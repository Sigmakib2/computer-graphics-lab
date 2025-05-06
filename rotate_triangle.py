import turtle, math

def draw(pts):
    turtle.penup()
    turtle.goto(pts[0])
    turtle.pendown()
    for x, y in pts[1:]+[pts[0]]:
        turtle.goto(x, y)

def rotate_about(pts, ang, px, py):
    θ = math.radians(ang)
    out = []
    for x, y in pts:
        dx, dy = x-px, y-py
        out.append((dx*math.cos(θ)-dy*math.sin(θ)+px,
                    dx*math.sin(θ)+dy*math.cos(θ)+py))
    return out

turtle.speed(0)
tri = [(0,0),(80,0),(40,60)]
draw(tri)
pivot = (120, 40)
turtle.penup(); turtle.goto(pivot); turtle.dot()
turtle.pendown()
draw(rotate_about(tri, 45, *pivot))
turtle.done()
