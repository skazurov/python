import turtle, math

turtle.shape('turtle')

turtle.color("black","yellow")

turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.color("black","blue")

turtle.penup()
turtle.goto(-35, 110)
turtle.pendown()

turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(35, 110)
turtle.pendown()

turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 95)
turtle.pendown()

turtle.color("black","black")
turtle.width(5)
turtle.goto(0, 60)

turtle.penup()
turtle.goto(30, 50)
turtle.pendown()

turtle.color("red","black")
turtle.right(90)
turtle.circle(-30, 180)
