
from time import sleep


nome= str(input('Digite seu nome completo: ')).strip
print('Analisando seu nome...')
sleep(2)
print('seu nome em letra maiuscula fica :',nome.upper())
print('seu nome em letra minuscula fica: ',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count('  ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))