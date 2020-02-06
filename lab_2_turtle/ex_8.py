import turtle

turtle.shape('turtle')

def make_square(s:int):
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s + 5)
    turtle.left(90)
    turtle.forward(s + 5)
    turtle.left(90)

s = 0

for i in range(10):

    make_square(s)
    s += 10
    
