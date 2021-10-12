#Import Turtle and Set Up Turtle Pen
from turtle import *
t = Pen()
t.hideturtle()

#Move Turtle Pen Forward -
t.fd(200)

#Move Turtle Pen Backward -
t.bk(280)

#Move Turtle Right -
t.rt(120)
t.fd(210)

#Move Turtle Left -
t.lt(120)
t.fd(210)

#Move Turtle Pen Up and Down -
t.pu()
t.fd(250)
t.rt(120)
t.pd()
t.fd(100)

#Move Turtle Back to Starting Position
t.home()
t.hideturtle()

#A Circle
t.circle(120)
t.circle(100)
t.circle(80)

#A circle with a second param
t.circle(180, 180) #Semicircle
t.circle(130, 90) #Quarter Circle
#Basically, for how many degrees should the circle continue.
#360 is default

#Clear the board
t.clear()
