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
    if pos_tortue > 6:
        return False
    else : return True
        
def frequence(précision: int, fonction) -> int:
    assert précision > 0
    Lievre = 0
    for x in range(précision):
        if fonction():
            Lievre += 1
    Pourcentage = (Lievre/précision)*100
    return Pourcentage

#print(frequence(154000000, lievre_gagne))
#exo_35(int(input('Nombre de départ \n')),int(input("Nombre de fin \n")))
#for x in range(10):
 #   print(lievre_gagne())





def inverse_plus_un(binaire):
    inverse = ''
    for bit in binaire:
        inverse += '0' if bit == '1' else '1'
    # Ajouter 1 au binaire inversé
    inverse = list(inverse)
    for i in range(len(inverse) - 1, -1, -1): 
        if inverse[i] == '0':
            inverse[i] = '1'
            break
        else:
            inverse[i] = '0'
    return ''.join(inverse)

# Testons l'algorithme
binaire = '0100'
resultat = inverse_plus_un(binaire)
print(f"L'inverse de {binaire} plus 1 est {resultat}")

def convert_base_10_to_x(decimal, base_x):
    if decimal == 0:
        return "0"  # Le nombre 0 reste inchangé dans n'importe quelle base.

    result = ""
    while decimal > 0:
        remainder = decimal % base_x
        result = str(remainder) + result  # Ajoutez le chiffre dans la bonne position.
        decimal = decimal // base_x  # Division entière pour continuer avec le quotient.
    return result

def banque_gagne():
    P = randint(1,6) + randint(1,6)
    if P == 2 or P == 3 or P == 12:
        return True
    elif P == 7 or P == 11:
        return False
    while True :
        S = randint(1,6) + randint(1,6)
        if S == 7:
            return True
        elif S == P:
            return False

print(frequence(1540000, banque_gagne))