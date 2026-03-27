import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("black")


def drawstars(n):
    for _ in range(n):
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(0, 300))
        t.dot(random.randint(2, 4), "white")

def drawbuilding(x, width, height):
    t.penup()
    t.goto(x, -200)
    t.pendown()
    t.color("gray")
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()

    drawwindows(x, width, height)


def drawwindows(x, width, height):
    for i in range(int(width // 20)):
        for j in range(int(height // 20)):
            if random.choice([True, False]):
                t.penup()
                t.goto(x + i*20 + 5, -200 + j*20 + 5)
                t.dot(8, "yellow")


drawstars(200)

x = -300
while x < 300:
    w = random.randint(40, 80)
    h = random.randint(100, 300)
    drawbuilding(x, w, h)
    x += w + 10

turtle.done()
