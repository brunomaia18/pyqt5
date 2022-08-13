nome = str(input("Digite seu nome completo: ")).strip().split()

print('Muito prazer em te conhecer..')
print("seu Primeiro nome é",nome[0])
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))
