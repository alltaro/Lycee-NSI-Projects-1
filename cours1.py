axes_x = [0.1*i for i in range(11)]

def f(x):
    return x+1
images = [f(x) for x in axes_x]
print(images)

def difference(t):
    return [t[i+1] - t[i] for i in range(len(t))]


def cube(n:int)-> list:
    return [i**3 for i in range(1,n+1)]

ligne = '12;11;-1'

def température():
    return [int(ligne.split(";")[x]) for x in range(len(ligne.split(";")))]
def temperature_valeur():
    return [int(valeur) for valeur in ligne.split(";")]



def est_palidrome(txt:str):
    txt = txt.lower()
    txt = txt.replace(" ", "")
    txt = txt.replace(",", "")
    txt = list(txt)
    return all(txt[x] == txt[len(txt) - x - 1] for x in range(len(txt)//2))

print(est_palidrome("Salut tula"))
print(température())

