from math import *
u = 3000
n = 0

while u >= 2000:
    u = 0.95 * u + 76
    n = n+1
    print("============================")
    print("valeur u:", u)
    print("valeur n:", n)
r = 2017 + n
print("============================")
print()
print("Le nombre d'abonnés arrêtera de chuter au rang", n)
print("Le nombre d'abonnés passera en dessous de 2000 en", r)

