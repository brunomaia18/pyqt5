from time import sleep
import random


print("-"*10)
print('''SUAS OPÇÔES:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
print("-"*10)
intes = ("PEDRA","PAPEL","TESOURA")
opçao = int(input("ESCOLHA UM: "))
ale = random.randint(0,2)

print("JO")
sleep(2)
print("KEN")
sleep(2)
print('''PO!!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
print("O COMPUTADOR JOGOU {}".format(intes[ale]))
print("O JOGADOR JOGOU {}".format(intes[opçao]))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

if ale == 0:
    if opçao == 0:
        print("EMPATE")
    elif opçao == 1 :
        print("PARABENS VOCÊ GANHOU!!")
    elif opçao == 2:
        print("VOCÊ PERDEU!!")
elif ale == 1: 
    if opçao == 0:
        print("VOCÊ PERDEU!!")
    elif opçao == 1 :
        print("EMPATE")
    elif opçao == 2:
        print("PARABENS VOCÊ GANHOU!!")
elif ale == 2:
    if opçao == 0:
        print("PARABENS VOCÊ GANHOU!")
    elif opçao == 1:
        print("VOCÊ PERDEU!!")
    elif opçao == 2:
        print("EMPATE")
        
