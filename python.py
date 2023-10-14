#tant que n > 1 diviser n par 10 et ajouter 1 à div puis renvoyer
from random import randint

def division(n:int)-> int:
    assert n > O
    div = 0
    while n>1:
        n /= 10
        div += 1
    return div
    
def binaire(n):
    chaine = ''
    while n > 0:
        chaine = str(n%2) + chaine
        n //= 2
    return chaine

def exo_35(a, b):
    assert a < b < 1000
    somme = 0
    for num in range(a,b+1):
        if num%2 != 0:
            somme += num
    print(somme)

def exo_35_while(a,b):
    assert a < b < 1000
    somme = 0
    nombre = a if a % 2 != 0 else a + 1
    while nombre <= b:
        somme += nombre
        nombre += 2
    return somme

def lievre_gagne():
    pos_tortue = 0
    de = 0
    while pos_tortue != 6:
        de = randint(1,6)
        if de != 6:
            pos_tortue += 1
        else :
            return "lievre"
    return "tortue"
        

#exo_35(int(input('Nombre de départ \n')),int(input("Nombre de fin \n")))
