import turtle, math

turtle.shape('turtle')

def make_polygon(a:int, n:int):

    alfa = 360 / n 

    for j in range(n):
        
        turtle.left(alfa)
        turtle.forward(a)
       
        
x = 0

n = 3
a = 15

for i in range(10):

    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    
    
    make_polygon(a, n)

    x += 2


    n += 1
    a += 5

