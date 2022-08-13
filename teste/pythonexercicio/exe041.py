from datetime import *
nascimento = int(input("qual o ano que você nasceu :"))

tempo = datetime.now()
anoatual = int(tempo.strftime("%Y"))
idade = anoatual - nascimento

if idade <= 9 :
    print("Você tem {} ".format(idade))
    print("Classificação: MIRRIM")
elif 9 < idade <= 14: 
    print("Você tem {} ".format(idade))
    print("Classificação: INFANTIL")
elif 14 < idade <= 19:
    print("Você tem {} ".format(idade))
    print("Classificação: JUNIOR")
elif 19 <= idade <= 25:
    print("Você tem {} ".format(idade))
    print("Classificação: SENIOR")
else:
    print("Você tem {} ".format(idade))
    print("Classificação: MASTER")