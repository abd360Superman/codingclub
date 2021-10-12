from turtle import *
t = Pen()
screen = Screen()

def f():
    t.fd(50)

def b():
    t.bk(50)

#On Keys
screen.onkey(f, "Up")
screen.onkey(b, "Down")
screen.listen()
