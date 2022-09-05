import turtle, random

wn = turtle.Screen()
wn.screensize(600, 600)

paint = turtle.Turtle('turtle')
colors = ['Red', 'Yellow', 'Green', 'Blue']
paint.width(turtle.numinput('width', 'Type line size (in numbers): '))
paint.speed(0)

# Arrow-Keys control function
def up():
    paint.setheading(90)
    paint.forward(100)

def down():
    paint.setheading(270)
    paint.forward(100)

def left():
    paint.setheading(180)
    paint.forward(100)

def right():
    paint.setheading(0)
    paint.forward(100)

# Color change
def colorChange():
    paint.color(random.choice(colors))

# Size change
def size():
    paint.pensize(1)

# Mouse Control (Clear + Drag) function
def clearScreen(x, y):
    paint.clear()

def dragging(x, y):
    paint.ondrag(None)
    paint.setheading(paint.towards(x, y))
    paint.goto(x, y)
    paint.ondrag(dragging)

# Shapes with random size
def square():
    for i in range(4):
        paint.forward(50)
        paint.left(90)

def circle():
    paint.circle(random.randrange(50, 100))

def rectangle():
    for i in range(2):
        paint.forward(50)
        paint.left(90)
        paint.forward(100)
        paint.left(90)

turtle.listen()

# Key-events

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.onkey(size, 'q')

turtle.onkey(colorChange, 'c')

# Mouse-events
turtle.onscreenclick(clearScreen, 3)
paint.ondrag(dragging)

# Shape-events
turtle.onkey(square, 's')
turtle.onkey(circle, 'o')
turtle.onkey(rectangle, 'r')

turtle.mainloop()