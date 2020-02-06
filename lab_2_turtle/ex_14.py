import turtle

turtle.shape('turtle')

def draw_star(n, length):
    if n % 2 != 0:
        for i in range(n):
            turtle.forward(100)
            a = n // 2 * 360 / n 
            turtle.left(a)

draw_star(5, 100)

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

draw_star(11, 100)
