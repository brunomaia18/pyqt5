frase = str(input("Digite uma frase : ")).upper().strip()

print("A letra A aparece {} vezes na frase".format(frase.count('A')))
print("Ela aparece na posiçao {} pela primeira vez".format(frase.find("A")+1))
print("Ela aparece na posiçao {} pela ultima vez".format(frase.rfind("A")+1))

