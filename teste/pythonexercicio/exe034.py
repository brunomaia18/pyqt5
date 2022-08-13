salario = int(input("Digite o seu salario atual : "))

if salario <=1200:
    aumento = salario + (salario * 15/100)
    print("Seu salario com o reajuste ficou R${}".format(aumento))
else:
    aumento = salario + (salario * 10/100)
    print("Seu salario com o reajuste ficou R${}".format(aumento))