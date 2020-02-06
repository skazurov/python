import turtle

turtle.shape('turtle')

def make_ray(a:int):
    turtle.right(a)
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180 + a)
    
n = 12
a = 0

for i in range(n):

    make_ray(a)
    a += 30
    
