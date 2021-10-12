from turtle import *
t = Pen()
t.hideturtle()

#Changing Pen Width
t.width(10)
t.fd(200)
t.rt(150)

t.width(5)
t.fd(200)
t.rt(150)

t.width(1)
t.fd(200)

#Changing Pen Colour
t.color("red", "green") #Red as pen color, green as fill color
t.rt(180)
t.begin_fill() #Called before filling a shape
t.circle(200)
t.end_fill() #Fill the shape drawn

#Select a background color
screen = Screen()
screen.bgcolor("red")

