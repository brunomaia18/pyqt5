dias = int(input("Quantos dias alugado ? "))
km = int(input("Quantos Km rodado ? "))

diaria = (dias*60) + (km*0.15)

print("O total a pagar è de R${:.2f}".format(diaria))

