#CONVERTENDO NUMERO PARA BINARIO , OCTAL, HEXAGONAL
numero = int(input("Digite um numero: "))
print('''Escolha uma Base para conversão:
      [1] Converter para Base BINARIA
      [2]Converter para Base OCTAL
      [3]Converter para Baase HEXAGONAL''')
opçao = int(input("Digite sua Opção: "))

if opçao == 1:
    print("O numero {} em BINARIO fica {}".format(numero, bin(numero)[2:]))
elif opçao == 2: 
    print ("o numero {} em  OCTAL FICA {}".format(numero,oct(numero)[2:]))
elif opçao == 3: 
    print("o numero {} em HEXAGONAL FICA {}".format(numero,hex(numero)[2:]))
else: 
    print("Essa opção não existe!!!")  
      