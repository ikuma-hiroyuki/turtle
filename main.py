import random
from turtle import Screen, Turtle

colors = ["medium blue", "lime", "deep pink", "indigo", "gold", "medium spring green", "olive drab", "dodger blue"]
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(turtle: Turtle, corners):
    angle = 360 / corners
    for _ in range(corners):
        turtle.forward(100)
        turtle.left(angle)


def draw_dash(turtle: Turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_random_walk(turtle: Turtle):
    turtle.pensize(10)
    turtle.color(random_color())
    turtle.forward(20)
    turtle.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim = Turtle("turtle")
tim.speed(0)
screen = Screen()
screen.colormode(255)

# tim.color("red")

# draw_dash(tim)
# for _ in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(tim, _)

# for _ in range(100):
#     draw_random_walk(tim)

draw_spirograph(5)

screen.exitonclick()
