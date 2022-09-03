numero = 0
cont = 0
soma = 0

while numero != 999:
      numero = int(input("Digite um numero [999 para parar]: "))
      cont = cont + numero
      soma += 1
x = cont - 999
print(f"Você digitou {soma-1} numeros e a soma deles é {x}")
