from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(600, 500)
pantalla.screensize(400, 500)

tortuga = Turtle()
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)

tortuga.penup()

tortuga.left(135)
tortuga.forward(70)
tortuga.pendown()

tortuga.right(45)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()