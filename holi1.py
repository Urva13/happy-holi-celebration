import turtle
import random

turtle.setup(1280,720)

wn=turtle.Screen().bgcolor("hotpink")

t=turtle.Turtle()

t.pensize(12)

def pdraw():

 t.right(90)

 for _ in range(90):

    t.forward(1)

    t.right(2)

def idraw():

    t.forward(20)

    t.backward(10)

    t.right(90)

    t.forward(100)

    t.right(90)

    t.forward(10)

    t.backward(20)

t.color("#CD0000")

t.penup()

t.goto(-500,0)

t.pendown()

t.left(90)

t.forward(100)

t.goto(-500,0)

t.penup()

t.right(90)

t.forward(70)

t.pendown()

t.left(90)

t.forward(100)

t.backward(50) 

t.left(90)

t.forward(70)

t.color("#000080")

t.penup()

t.goto(-400,0)

t.pendown()

t.left(250)

t.forward(110) 

t.right(140)

t.forward(110)

t.penup()

t.goto(-385,40)

t.pendown()

t.left(70)

t.forward(45)

t.color("cyan")

t.penup()

t.goto(-300,0)

t.pendown()

t.left(90)

t.forward(100)

pdraw()

t.color("#ffff00")

t.penup()

t.goto(-250,0)

t.pendown()

t.right(90)

t.forward(100)

pdraw()

t.color("#551A8B")

t.penup()

t.goto(-180,0)

t.pendown()

t.right(90)

t.forward(60)

t.left(45)

t.forward(50)

t.backward(50)

t.right(90)

t.forward(50)

t.color("#EE0000")

t.penup() 

t.goto(-50,0) 

t.pendown()

t.left(45)

t.forward(100)

t.goto(-50,0)

t.penup()

t.right(90)

t.forward(70)

t.pendown()

t.left(90)

t.forward(100)

t.backward(50)

t.left(90)

t.forward(70) 

t.color("#800080")

t.penup()

t.goto(90,90)

t.pendown()

t.right(180)

for _ in range(180):

    t.forward(1.7)

    t.right(2)

t.color("#27408b")

t.penup()

t.goto(160,100)

t.pendown()

t.right(90)

t.forward(100)

t.left(90)

t.forward(70)

t.color("#308014")

t.penup()

t.goto(260,100)

t.pendown()

t.forward(40)

t.backward(20)

t.right(90)

t.forward(100)

t.left(90)

t.forward(20)

t.backward(40)

t=turtle.Turtle()

def pen(colour):

    t.color(colour)

def fireworks(distance):

    for _ in range(30):

        t.forward(distance)

        t.right(180-(360/20))

def move():

    t.penup()

    x=random.randint(-700,700)

    y=random.randint(-700,700)

    t.goto(x,y)

    t.pendown()

t.speed(0)

colors = ['WHITE','BLACK','VIOLET','CYAN','PINK','RED','ORANGE','GREEN','YELLOW','BLUE']

for i in range(50):

    color=random.choice(colors)

    pen(color)

    fireworks(random.randint(50,100))

    move()

turtle.done()