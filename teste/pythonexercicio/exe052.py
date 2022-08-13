#Sabendo se o numero é primo

primo = int(input("Digite um numero para saber se ele é primo: "))
count = 0

for c in range(1,primo+1):
    if primo % c == 0 and primo % primo == 0:
        print('\033[34m', end= " ")
        count += 1
    else:
        print('\033[33m', end=" ")
    print('{}'.format(c), end = " ")
    
print("\n\033[37mO numero {} foi divisivil {} vezes ".format(primo,count))

if count == 2 :
    print("Por isso ele è PRIMO")
else:
    print("Por isso ele NÃO È PRIMO")