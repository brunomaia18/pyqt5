ano = int(input("Digite um ano, para saber se e BISSEXTO: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print("o ano {} è BISSEXTo".format(ano))
else: 
    print("O ano {} não é BISSEXTO".format(ano))