def inverse_hexa(nombre_hexa):
    # Convertir le nombre hexadécimal en entier
    nombre = int(nombre_hexa, 16)
    
    # Inverser les bits du nombre
    nombre_inverse = ~nombre
    
    # Convertir le nombre inversé en hexadécimal
    nombre_hexa_inverse = hex(nombre_inverse & 0xFFFFFFFF)[2:]
    
    return nombre_hexa_inverse.zfill(len(nombre_hexa))

def negatif_hexa(nombre_hexa):
    # Convertir le nombre hexadécimal en entier
    nombre = int(nombre_hexa, 16)
    
    # Trouver le négatif du nombre
    nombre_negatif = -nombre
    
    # Convertir le nombre négatif en hexadécimal
    nombre_hexa_negatif = hex(nombre_negatif & 0xFFFFFFFF)[2:]
    
    return nombre_hexa_negatif.zfill(len(nombre_hexa))

def convertir_base_x_a_10(nombre, base):
    return int(nombre, base)


def convert_to_base_10(number, base):
    number = str(number)
    length = len(number)
    result = 0
    for i, digit in enumerate(number):
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit.upper()) - ord('A') + 10
        power = length - i - 1
        result += value * (base ** power)
    return result

# Exemple d'utilisation :
print(convert_to_base_10('7DE', 16))  # Affiche : 2014

print(inverse_hexa('3cff'))  # Affiche 'c3'
print(negatif_hexa('0010'))  # Affiche 'fff0'
