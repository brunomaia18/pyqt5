valor = float(input("Qual o valor do produto : R$"))

desconto_ganho = valor * 0.05
desconto_total = round(valor - desconto_ganho)
print("Valor total é R$ {} com desconta fica {}".format(valor,desconto_total))