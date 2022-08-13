pesomenor =0
pesomaior = 0
count = 0 
for i in range(1,5+1):
    peso = float(input(f"Peso da {i}º pessoa: "))
    if i == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        elif pesomenor > peso:
            pesomenor = peso
print(f'O maior peso é {pesomaior}KG')
print(f'O menor peso é {pesomenor}KG')


