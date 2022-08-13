#Somando numeros pares:
count = 0
soma = 0
for c in range(0,6):
    numero = int(input("Digite um numero : "))
    if numero % 2 == 0:
        soma = soma + numero
        count = count + 1
print("No total temo {} numeros pares e a soma deles é {}".format(count,soma))