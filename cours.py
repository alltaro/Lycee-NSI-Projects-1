from tkinter import *
from random import randint

NB_CELLULES  = 500
NB_GENERATIONS = 400

###############################################
#
# Partie 1 : Automates cellulaires bicolores
#
################################################


def dec_to_bin(nombre:int,taille:int)->list:
    """
    convertit un nombre dÃ©cimal en binaire
    renvoie un tableau de longueur taille
    """
    tab = []
    while nombre > 0:
        tab.append(nombre % 2)
        nombre //= 2
    return tab + [0]*(taille-len(tab))

def indice(gauche:int,centre:int,droit:int)->int:
    """
    renvoie l'indice compris entre 0 et 7 formÃ©
    Ã  partir des Ã©tats de la cellule et des
    voisines Ã  gauche et Ã  droite
    si la cellule est vivante donc 1
    et si sa voisine de gauche est vivante donc 1
    et si sa voisine de droite est morte donc 0
    on a donc 1,1,0 qui donne 6 en dÃ©cimal
    """
    if gauche == 0 and centre == 0 and droit == 0:
        return 0
    if gauche == 0 and centre == 0 and droit == 1:
        return 1
    if gauche == 0 and centre == 1 and droit == 0:
        return 2
    if gauche == 0 and centre == 1 and droit == 1:
        return 3
    if gauche == 1 and centre == 0 and droit == 0:
        return 4
    if gauche == 1 and centre == 0 and droit == 1:
        return 5
    if gauche == 1 and centre == 1 and droit == 0:
        return 6
    if gauche == 1 and centre == 1 and droit == 1:
        return 7
    

###############################################
#
# Fonctions communes Ã  tous les automates 1D
#
################################################

def etat_suivant(col_actuelle:list,regle:list,pos:int,voisinage)->int:
    """
    renvoie l'Ã©tat futur de la cellule situÃ©e
    dans le tableau col_actuelle à  la position pos
    en tenant compte de la règle et du voisinage
    """
    return regle[voisinage(col_actuelle[pos-1],
                           col_actuelle[pos],
                           col_actuelle[pos+1])]

def generation_suivante(col_actuelle:list,regle:list,voisinage)->list:
    """
    renvoie la génération suivante de la colonie actuelle
    """
    n_generation = [0]*len(col_actuelle)
    for pos in range(1,len(col_actuelle)-1):
       n_generation[pos] = etat_suivant(col_actuelle,regle,pos,voisinage)
    return n_generation

def initialisation()->list:
    """
    renvoie un tableau de taille NB_CELLULES
    ne contenant que des 0 et
    oÃ¹ on a insÃ©rÃ© un 1 au milieu
    """
    Tableau = [0]*NB_CELLULES
    Tableau[NB_CELLULES//2] = 1
    return Tableau

def evolution(regle:list,voisinage,dessine_col)-> None:
    """
    on gÃ©nÃ¨re NB_GENERATIONS colonies
    et on dessine chaque colonie l'une en dessous de l'autre
    avec la fonction dessine_col qui a deux paramÃ¨tres
    -la colonie actuelle
    -l'indice de la colonie (la premiÃ¨re colonie est d'indice 0)
    """
    colonie_actuelle = initialisation()
    dessine_col(colonie_actuelle,0)
    for num_col in range(1,NB_GENERATIONS):
        colonie_suivante = generation_suivante(colonie_actuelle, regle, voisinage)
        dessine_col(colonie_suivante, num_col)
        colonie_actuelle = colonie_suivante

###############################################
#
# Partie 2 : Automates cellulaires tricolores
#
################################################

def dec_to_tri(nombre:int)->list:

    """
    convertit un nombre dÃ©cimal en base 3 sur 7 chiffres
    renvoie un tableau de longueur 7
    >>> dec_to_tri(2040)
    2210120
    """
    pass

def indice_tri(gauche:int,centre:int,droit:int)->int:
    """
    renvoie l'indice compris entre 0 et 6 formÃ©
    Ã  partir des Ã©tats de la cellule et des
    voisines Ã  gauche et Ã  droite
    en faisant la somme des Ã©tats
    """
    pass

#-------------------------------------------------------------
#
#   NE RIEN ECRIRE DANS LA PARTIE CI_DESSOUS JUSQU'AU MAIN
#
#-------------------------------------------------------------
# Marge autour du Canevas
MARGE   = 10

# Largeur d'une Cellule
COTE    = 2

# Dimensions du Canevas
LARGEUR = 2*MARGE + NB_CELLULES*COTE
HAUTEUR = 2*MARGE + NB_GENERATIONS*COTE



def dessineCarre(colonie,numGen,numCel):
   x = MARGE + numCel*COTE
   y = MARGE + numGen*COTE
   if colonie[numCel]:
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE,fill="black")
   else:
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE)

def dessineCarreTri(colonie,numGen,numCel):
   x = MARGE + numCel*COTE
   y = MARGE + numGen*COTE
   if colonie[numCel] == 2:
       #couleur = noir
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE,fill="#000000",outline="#000000")
   elif colonie[numCel] == 1:
       #couleur = gris
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE,fill="#7f7f7f",outline="#7f7f7f")
   else:
       #couleur blanc
       zoneDessin.create_rectangle(x,y,x+COTE,y+COTE,fill="#ffffff",outline="#ffffff")

def dessine_colonie(colonie,numGen):
    for i in range(len(colonie)):
        dessineCarre(colonie,numGen,i)

def dessine_colonie_tri(colonie,numGen):
    for i in range(len(colonie)):
        dessineCarreTri(colonie,numGen,i)


# ############################################
#
#               ------- MAIN------
#
###############################################


###############################################
#
# Partie 1 : Automates cellulaires bicolores
#

fenetre = Tk()
fenetre.title("automate cellulaire bicolore")
#
#
#
zoneDessin = Canvas(fenetre,width=LARGEUR,height=HAUTEUR)
zoneDessin.pack(side=TOP)
#
regle = dec_to_bin(69,8)
evolution(regle,indice,dessine_colonie)
fenetre.mainloop()


###############################################
#
# Partie 2 : Automates cellulaires tricolores
#
################################################

#----------------------------------------------------------
#fenetre = Tk()
#fenetre.title("automate cellulaire tricolore")
#zoneDessin = Canvas(fenetre,width=LARGEUR,height=HAUTEUR)
#zoneDessin.pack(side=TOP)
#

#regle = dec_to_tri(2049)
#evolution(regle,indice_tri,dessine_colonie_tri)
#fenetre.mainloop()