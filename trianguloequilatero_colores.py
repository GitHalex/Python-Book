from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

tortuga = Turtle()
#Agregando un tamaño de pinzel a 10
tortuga.pensize(10)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)

pantalla.exitonclick()