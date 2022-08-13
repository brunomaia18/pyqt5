   #Sabendo se a palavra e um polindromo ou não:
frase = str(input("Digite uma frase pra ver se é um polimetro : ")).upper().strip()
palavra = frase.split()
junto =  "".join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print("A frase {} fica {} ao contrario".format(junto,inverso))
if inverso == junto:
    print("Temos um políndromo")
else:
    print("Não é um políndromo")