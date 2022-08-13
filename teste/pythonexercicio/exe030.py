from random import *
numero = int(input("Escolha um numero : "))
#se o resto da divisao for 0 e par, se nao vai ser impar
resultado = numero % 2

if resultado == 0:
    print("O numero {} é PAR".format(numero))
else:
    print("O numero {} é IMPAR".format(numero))