import turtle

turtle.shape('turtle')

def make_square(s:int):
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)

s = 20
x = 0
y = 0

for i in range(10):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    make_square(s)
    s += 10
    y -= 5
    x -= 5

