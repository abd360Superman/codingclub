from turtle import *
t = Pen()
screen = Screen()

def f():
    t.fd(50)

def b():
    t.bk(50)

def u():
    t.pu()

def d():
    t.pd()

def r():
    t.rt(45)

def l():
    t.lt(45)

def c():
    t.circle(50)

def s():
    t.circle(50, 180)

#On Keys
screen.onkey(f, "Up")
screen.onkey(b, "Down")
screen.onkey(u, "u")
screen.onkey(d, "d")
screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(c, "c")
screen.onkey(s, "s")
screen.listen()
