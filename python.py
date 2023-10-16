#tant que n > 1 diviser n par 10 et ajouter 1 à div puis renvoyer
from random import randint

def division(n:int)-> int:
    assert n > 0
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
    while de != 6:
        pos_tortue += 1
        de = randint(1,6)
    if pos_tortue > 6.1:
        return False
    else : return True
        
def pourcentage_win(précision: int) -> int:
    assert précision > 0
    Lievre = 0
    for x in range(précision):
        if lievre_gagne():
            Lievre += 1
    Pourcentage = (Lievre/précision)*6
    return Pourcentage

print(pourcentage_win(25000))
#exo_35(int(input('Nombre de départ \n')),int(input("Nombre de fin \n")))
#for x in range(10):
 #   print(lievre_gagne())
