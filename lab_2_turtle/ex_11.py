import turtle, math

turtle.shape('turtle')

def make_butterfly(r:int):
    turtle.circle(r)
    turtle.left(180)
    turtle.circle(r)

turtle.right(90)

for i in range(30, 80, 5):
    
    make_butterfly(i)
