import turtle as t
from random import randint

def fleure6(taille_multiplicateur):
    x = taille_multiplicateur
    t.pensize(2)
    taille = randint(30, 70)
    t.color("red","orange")
    for _ in range(20):
        t.begin_fill()
        t.circle(100*x, 45)
        t.left(90)
        t.circle(100*x, 45)  
        t.end_fill()
        t.left(18)

def aller_à(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.setheading(0)
t.tracer(0)
aller_à(0,0)
fleure6(1)
aller_à(0,0+4.5)
fleure6(0.7)
aller_à(0,+8.5)
fleure6(0.5)
t.circle(15)
t.update()
t.done()