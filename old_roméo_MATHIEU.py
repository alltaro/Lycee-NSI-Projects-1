from random import randint
import turtle as t
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////
divide_orientation_circle = 1
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
longueur = 30
cran = [4, 13, 25, 40,0]
valeur = [7, 4, 1.75, 0.75, 0.50]
pos_x = []
pos_y = []
fenetre = t.Screen()
fenetre.setup(width=fenetre.window_width(), height=fenetre.window_height())
largeur = fenetre.window_width()
hauteur = fenetre.window_height()


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
def rosace(n):
    t.tracer(0)
    if n == 1:
        print(1)
        for _ in range(15):
            t.pencolor(colors[_%6])
            t.fillcolor(colors[_%6])
            carré(longueur*2)
            carré(longueur/3*2*2)
            t.right(360/15)
    elif n == 2:
        for i in range(36):
            t.pencolor(colors[i%6])
            t.fillcolor(colors[i%6])
            losange(longueur*1.65)
            t.right(10)
    elif n == 3:
        for i in range(20):
            t.pencolor(colors[i%6])
            t.fillcolor(colors[i%6])
            t.begin_fill()
            losange(longueur*1.5)
            t.right(360/20)
            t.end_fill()
    elif n == 4:
        t.pensize(1)
        t.color(colors[randint(0,5)], colors[randint(0,5)])
        t.begin_fill()
        t.forward(100)
        t.left(130)
        for _ in range(49):
            t.forward(200)
            t.left(130)
        t.forward(100)
        t.left(130)
        t.end_fill()
    else :
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
    t.tracer(1)
        

def dessiner_tige():
    tige_orientation = randint(-60,60)
    print(tige_orientation)
    taille_tige = randint(25, 38)
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
    


def bouquet():
    retour_au_départ()
    nombre_fleurs = randint(6,12)
    for i in range(nombre_fleurs):
        t.pencolor("green")
        t.setheading(90)
        t.pensize(randint(3,5))
        dessiner_tige()
        pos_x.append(str(t.xcor))
        pos_y.append(str(t.ycor))
        print(pos_x)
        retour_au_départ()
    for i in range(nombre_fleurs):
        t.pencolor(colors[i%6]) 
        t.fillcolor(colors[i%6])
        t.goto(pos_x[i](),pos_y[i]())
        t.pensize(randint(2,3))
        rosace(randint(1,5))
        retour_au_départ()
        

bouquet()