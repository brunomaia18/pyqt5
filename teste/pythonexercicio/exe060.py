import math

numero = int(input('''Digite um numero
para saber o seu fatorial: '''))
factor = math.factorial(numero)
cont = numero
print(f"Calculando {numero}!: ",end=" ")
while cont > 0:
  print(f"{cont}", end=' ')
  print("x" if cont > 1 else "=", end=" "  )
  cont -= 1

print(f"{factor}", end=' ')
