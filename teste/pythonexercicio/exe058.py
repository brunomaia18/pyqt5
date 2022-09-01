import random

computador = random.randint(0,10)
print("Sou o seu computador...")
print("Estou pensando em um numero entre 0 a 10..")
acertou = False
cont = 0

while not acertou:
     jogo = int(input("Diga o seu palpite: "))
     if jogo == computador:
          print("Parabens você acertou")
          acertou = True
     elif jogo < computador:
         print("Tente colocar um numero MAIOR \n tente NOVAMENTE")
         #jogo = int(input("tente NOVAMENTE: "))
     elif jogo > computador:
          print("Tente colocar um numero MENOR \n tente NOVAMENTE ")
         # jogo = int(input("tente NOVAMENTE: "))
     cont += 1

print(f"você acertou na {cont} tentativa, PARABENS")
