from datetime import *
ano = int(input("Qual o ano que voce nasceu : "))

tempo = datetime.now()

anoatual = int(tempo.strftime("%Y"))
a1 = anoatual
idade = a1 - ano
sub = 18 - idade 

anoalistamento = sub + anoatual

if idade < 18: 
    print ("Você nasceu em {} , você tem {} em {}". format(ano, idade ,  anoatual))
    print ("Faltam {} para voce se alistar, voce vai se alistar em {}".format(sub, anoalistamento))
elif idade == 18 :
    print ("Você nasceu em {} , você tem {} em {}". format(ano, idade ,  anoatual))
    print ("Você tem  {}  voce ja pode se  alistar".format(sub))
elif idade > 18:
     print("Você nasceu em {} , você tem {} em {}". format(ano, idade ,  anoatual))
     print ("Você ja passou do prazo de alistamento, procure um junta militar")
     