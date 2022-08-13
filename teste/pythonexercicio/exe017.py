import math
cateto_oposto = float(input("Comprimento do Cateto Oposto: "))
cateto_adjacente = float(input("Comprimento do Cateto adjacente: "))

h = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("A hipotenusa é {:.2f}".format(h))