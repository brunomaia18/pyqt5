radar = int(input("Qual a velocidade do seu carro : "))

print("Você está a {}Km/H".format(radar))

if radar >= 60 : 
    multa = (radar-60)*7
    print("Você ultrapassou o limite de velocidade..")
    print("vai ter que pagar uma multa de R${}".format(multa))
else:
    print("pode seguir ")