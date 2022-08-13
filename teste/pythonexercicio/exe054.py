#sabendo quem e de menor e quem e de maior
from datetime import *
date = datetime.now()
ano = int(date.strftime("%Y"))
count = 0
totmaior = 0
totmenor = 0
for c in range (0,7):
    count += 1
    nascimento = int(input("Qual o ano a {}º pessoa nasceu: ".format(count)))
    idade = ano-nascimento

    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1
print("Ao todo tivemos {} pessoas maior de idade".format(totmaior))
print("Ao todo tivemos {} pessoas MENOR de idade".format(totmenor))