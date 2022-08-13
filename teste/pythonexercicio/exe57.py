
sexo = str(input("sexo [F/M]: ")).strip().upper()[0]
'''while sexo not in "MnFf":
    print("digite um valor correto")
    sexo = str(input("sexo [F/M]: ")).strip().upper()[0]

print(f"Você é do sexo {sexo}")'''

while sexo != "M" and sexo != "F":
    print("Valor invalido, tente novamente")
    sexo = str(input("sexo [F/M]: ")).strip().upper()[0]
