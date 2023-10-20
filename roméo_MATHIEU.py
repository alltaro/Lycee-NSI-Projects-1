from random import randint, uniform
import turtle as t
from turtle import *
import turtle
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////
divide_orientation_circle = 1
colors = ["#c72e20", "#d1992a", "#b7bf21", "#80bf28", "#22b385", "#2095c7", "#8f20c7", "#b01c72"]
#    rouge      orange            jaoune     vert     bleu foncé    violet      
longueur = 23
cran = [4, 13, 25,30,40,50,60,0]
vert = 4
valeur = [7.2, 4.8,3 ,2, 0.90,0.70,0.55,0.47]
coef_circle = 1.5*2*2*150
pos_x = []
pos_y = []
fenetre = t.Screen()
fenetre.setup(width=fenetre.window_width(), height=fenetre.window_height())
largeur = fenetre.window_width()
hauteur = fenetre.window_height()
angle_droit = 90
nombre_de_couleurs = 8
angle_1_losange = 60
origin_x = 0
origin_y = 1
angle_2_losange = 120
haut = 90
nombre_de_fleurs_min = 6
nombre_de_fleurs_max = 12
taille_tige_min = 2
taille_tige_max = 3
coef_fleur6_1 = 1
coef_fleur6_2 = 0.7
coef_fleur6_3 = 0.5
fleur6_taille_circle = 15
rayon_fleur6 = 100
angle_1_fleur6 = 90
angle_rosace_2_1 = 10
angle_2_fleur6 = 18
tour_complet = 360
quart_de_tour = 45
vitesse_tortue = 10
demi_tour= 180
coef_rosace_1 = 2
coef_rosace_2 = 3
coef_rosace_3 = 4
multiplicateur_rosace_3 = 1.5
nombre_de_répétitions_rosace_3 = 20
circle_1_rosace_4 = 30
circle_2_rosace_4 = 26
circle_3_rosace_4 = 20
circle_4_rosace_4 = 16
incli_min = -80
incli_max = 80


def aller_à(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def retour_au_départ():
    t.penup()
    t.goto(0, -largeur/2)
    t.pendown()

def carré(longueur):
    for _ in range(4):
        t.forward(longueur)
        t.right(angle_droit)

def losange(longueur):
    for _ in range(2):
                t.forward(longueur)
                t.right(angle_1_losange)
                t.forward(longueur)
                t.right(angle_2_losange)
                
def fleure6(taille_multiplicateur):
    x = taille_multiplicateur
    nombre_de_répétitions_fleur6 = 20
    t.pensize(2)
    t.color(colors[1],colors[2])
    for _ in range(nombre_de_répétitions_fleur6):
        t.begin_fill()
        t.circle(rayon_fleur6*x, quart_de_tour)
        t.left(angle_1_fleur6)
        t.circle(rayon_fleur6*x, quart_de_tour)  
        t.end_fill()
        t.left(angle_2_fleur6)
        

def rosace(n, i, pos_x_y):
    t.tracer(0)
    if n == 1:
        
        nombre_de_répétitions = 15
        for i in range(nombre_de_répétitions):
            t.pencolor(colors[i%nombre_de_couleurs])
            t.fillcolor(colors[i%nombre_de_couleurs])
            carré(longueur*coef_rosace_1)
            carré(longueur/coef_rosace_2*coef_rosace_3)
            t.right(tour_complet/nombre_de_répétitions)
    elif n == 2:
        taille = uniform(30, 60)
        for _ in range(9):
            begin_fill()
            circle(taille, angle_droit) 
            left(angle_droit)
            circle(taille, angle_droit)
            end_fill()
            left(angle_rosace_2_1)
    elif n == 3:
        for i in range(nombre_de_répétitions_rosace_3):
            t.pencolor(colors[i%nombre_de_couleurs])
            t.fillcolor(colors[i%nombre_de_couleurs])
            t.begin_fill()
            losange(longueur*multiplicateur_rosace_3)
            t.right(tour_complet/nombre_de_répétitions_rosace_3)
            t.end_fill()
    elif n == 4 :
        t.pensize(1)
        for i in range(8):
            t.fillcolor(colors[i%nombre_de_couleurs])
            t.begin_fill()
            t.circle(circle_1_rosace_4)
            t.end_fill()
            t.fillcolor("#ffffff")
            t.begin_fill()
            t.circle(circle_2_rosace_4)
            t.end_fill()
            t.fillcolor(colors[i%nombre_de_couleurs])
            t.begin_fill()
            t.circle(circle_3_rosace_4)
            t.end_fill()
            t.fillcolor("#ffffff")
            t.begin_fill()
            t.circle(circle_4_rosace_4)
            t.end_fill()
            t.rt(quart_de_tour)
    elif n == 5:
        t.begin_fill()
        t.pensize(1)
        for _ in range(45):
            t.forward(100/1.5)
            t.left(170)
            t.forward(100/1.5)
        t.end_fill()
    elif n == 6:
        if randint(1,2) == 2:
            t.color(colors[2],colors[3])
        t.setheading(0)
        aller_à(pos_x_y[i][origin_x],pos_x_y[i][origin_y])
        fleure6(coef_fleur6_1)
        aller_à(pos_x_y[i][origin_x],pos_x_y[i][origin_y]+4.5)
        fleure6(coef_fleur6_2)
        aller_à(pos_x_y[i][origin_x],pos_x_y[i][origin_y]+8.5)
        fleure6(coef_fleur6_3)
        t.circle(fleur6_taille_circle)
    t.tracer(1)
 
def dessiner_tige(): #cet algorithme va permettre de tordre plus ou moins les tiges en fonction de leur inclination
    tige_orientation = uniform(incli_min,incli_max)
    taille_tige = uniform(25, 38)
    if tige_orientation < 0:
        t.left(-tige_orientation)
        t.left(demi_tour)
        for i in range(len(cran)):
            if tige_orientation > -cran[i] or cran[i]==0:
                divide_orientation_circle = valeur[i]
                break
        t.circle(divide_orientation_circle*coef_circle,-taille_tige/divide_orientation_circle)
    else:
        t.right(tige_orientation)
        for i in range(len(cran)):
            if tige_orientation < cran[i] or cran[i]==0:
                divide_orientation_circle = valeur[i]
                break
        t.circle(divide_orientation_circle*coef_circle,taille_tige/divide_orientation_circle)
    
def organisation_des_points_par_ordre_croissant(x, y):
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
    t.speed(vitesse_tortue)
    nombre_fleurs = randint(nombre_de_fleurs_min,nombre_de_fleurs_max)
    for i in range(nombre_fleurs):
        t.pencolor(colors[vert])
        t.setheading(haut)
        t.pensize(randint(taille_tige_min,taille_tige_max))
        dessiner_tige()
        pos_x.append(t.xcor())
        pos_y.append(t.ycor())
        retour_au_départ()
    for i in range(nombre_fleurs):
        t.setheading(haut)
        t.color(colors[i%nombre_de_couleurs],colors[(i+1)%nombre_de_couleurs])
        pos_x_y = organisation_des_points_par_ordre_croissant(pos_x,pos_y)
        aller_à(pos_x_y[i][origin_x],pos_x_y[i][origin_y])
        t.pensize(randint(2,3))
        rosace(1+((i+fleur_de_départ)%6),i, pos_x_y)
        retour_au_départ()
        

bouquet()
done()