import math

angulo = float(input("Digite um ângulo que você deseja: "))

radians = math.radians(angulo)
seno = math.sin(radians)
cos = math.cos(radians)
tang = math.tan(radians)



print("O seno de {} é : {:.2f}".format(angulo, seno))
print("O cosseno de {} é : {:.2f}".format(angulo, cos))
print("O tangente de {} é : {:.2f}".format(angulo, tang))