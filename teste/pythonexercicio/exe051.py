print("==="*10)
print ('''    10 termos de uma PA''')
print("==="*10)

pt = int(input("Digite o Primeiro termo da PA: "))
razao = int(input("Digite a razão da sua PA: "))

for c in range(pt,pt+11,razao):
    print(c, end=" -> ")
print(end=" ACABOU ")