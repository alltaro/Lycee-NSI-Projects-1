from random import randint, uniform
import turtle as t
from turtle import *
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////
divide_orientation_circle = 1
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
longueur = 23
cran = [4, 13, 25, 40,0]
valeur = [7.6, 5, 2, 0.78, 0.50]
pos_x = []
pos_y = []
fenetre = t.Screen()
fenetre.setup(width=fenetre.window_width(), height=fenetre.window_height())
largeur = fenetre.window_width()
hauteur = fenetre.window_height()

def aller_à(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def retour_au_départ():
    t.penup()
    t.goto(0, -largeur/2)
    t.pendown()

def carré(longueur):
    t.forward(longueur)
    t.right(90)
    t.forward(longueur)
    t.right(90)
    t.forward(longueur)
    t.right(90)
    t.forward(longueur)
    t.right(90)

def losange(longueur):
    for j in range(2):
                t.forward(longueur)
                t.right(60)
                t.forward(longueur)
                t.right(120)
                
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
        

def rosace(n, i, pos_x_y):
    t.tracer(0)
    if n == 1:
        for i in range(15):
            t.pencolor(colors[i%6])
            t.fillcolor(colors[i%6])
            carré(longueur*2)
            carré(longueur/3*2*2)
            t.right(360/15)
    elif n == 2:
        taille = uniform(30, 70)
        for _ in range(9):
            begin_fill()
            circle(taille, 90)  # Utilisez random.uniform pour varier la taille
            left(90)
            circle(taille, 90)  # Utilisez random.uniform pour varier la taille
            end_fill()
            left(10)
    elif n == 3:
        for i in range(20):
            t.pencolor(colors[i%6])
            t.fillcolor(colors[i%6])
            t.begin_fill()
            losange(longueur*1.5)
            t.right(360/20)
            t.end_fill()
    elif n == 4 :
        t.pensize(1)
        for i in range(8):
            t.fillcolor(colors[i%6])
            t.begin_fill()
            t.circle(30)
            t.end_fill()
            t.fillcolor("white")
            t.begin_fill()
            t.circle(26)
            t.end_fill()
            t.fillcolor(colors[i%6])
            t.begin_fill()
            t.circle(20)
            t.end_fill()
            t.fillcolor("white")
            t.begin_fill()
            t.circle(16)
            t.end_fill()
            t.rt(45)
    elif n == 5:
        t.begin_fill()
        for _ in range(45):
            t.forward(100)
            t.left(170)
            t.forward(100)
        t.end_fill()
    elif n == 6:
        print(pos_x_y[i][0],pos_x_y[i][1])
        t.setheading(0)
        aller(pos_x_y[i][0],pos_x_y[i][1])
        fleure6(1)
        aller_à(pos_x_y[i][0],pos_x_y[i][1]+4.5)
        fleure6(0.7)
        aller_à(pos_x_y[i][0],pos_x_y[i][1]+8.5)
        fleure6(0.5)
        t.circle(15)
    t.tracer(1)
    

def dessiner_tige():
    tige_orientation = uniform(-70,70)
    taille_tige = uniform(25, 38)
    if tige_orientation < 0:
        t.left(-tige_orientation)
        t.left(180)
        for i in range(len(cran)):
            if tige_orientation > -cran[i] or cran[i]==0:
                divide_orientation_circle = valeur[i]
                break
        t.circle(150*divide_orientation_circle*1.5*2*2,-taille_tige/divide_orientation_circle)
    else:
        t.right(tige_orientation)
        for i in range(len(cran)):
            if tige_orientation < cran[i] or cran[i]==0:
                divide_orientation_circle = valeur[i]
                break
        t.circle(150*divide_orientation_circle*1.5*2*2,taille_tige/divide_orientation_circle)
    
def organisation_des_points(x, y):
    print(zip(x, y))
    points = list(zip(x, y))
    print(points)
    points_sorted = sorted(points, key=lambda point: point[1], reverse=True)
    liste_finale = [[x, y] for x, y in points_sorted]
    return liste_finale

def bouquet():
    fleur_de_départ = randint(0,5)
    t.tracer(0)
    retour_au_départ()
    t.speed(10)
    nombre_fleurs = randint(6,12)
    for i in range(nombre_fleurs):
        t.pencolor("green")
        t.setheading(90)
        t.pensize(randint(3,5))
        dessiner_tige()
        pos_x.append(t.xcor())
        pos_y.append(t.ycor())
        retour_au_départ()
    for i in range(nombre_fleurs):
        t.setheading(90)
        t.color(colors[i%6],colors[(i+1)%6])
        pos_x_y = organisation_des_points(pos_x,pos_y)
        aller_à(pos_x_y[i][0],pos_x_y[i][1])
        t.pensize(randint(2,3))
        rosace(1+((i+fleur_de_départ)%6),i, pos_x_y)
        retour_au_départ()
        

bouquet()




done()

