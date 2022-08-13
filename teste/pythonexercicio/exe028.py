import random

adv = int(input("Esoclha um numero de 0 a 5: "))

num = random.randint(0,5)


if adv == num : 
    print("parabéns você acertou...")
else:
    print('tente novamente')
    print(f"o numero era {num}")


print("Até a proxima...")