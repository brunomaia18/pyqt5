                    #Calculadora 2.0
numero = int(input("Digite um numero para ver a tabuada : "))
count = 0
for c in range(0,11):
    multi = numero*c
    count = count + 1
    print("{} X {} = {}".format(numero,count,multi))    