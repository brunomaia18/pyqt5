print("---"*10)
print("analisando triangulo")
print("---"*10)
r1 = float(input("Digite um segmento do: "))
r2 = float(input("Digite outro segmento do: "))
r3 = float(input("Digite outro segmento do: "))

if r1<r2+r3 and r2 <r3+r1 and r3 < r2+r1:
    print("Esses segmentos Formam um Triangulo")
else:
    print("Não forma um triangulo")