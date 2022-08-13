carteira = float(input("Quanto de dinheiro vc tem na carteira : R$ "))

conversao = round( carteira / 5,35)

print("Com R$ {} você pode comprar ${}".format(carteira,conversao))