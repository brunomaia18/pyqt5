from curses.ascii import isspace


variavel = input("Digite Algo : ")
print("O tipo primitivo desse valor é ".format(type(variavel)))
print("Só tem espaço :", variavel.isspace())
print("Isso é um Número :", variavel.isnumeric())
print("È Alfabetico :", variavel.isalpha())
print("É Alfanumerico:", variavel.isalnum())
print("È Maiusculo :", variavel.isupper())
print("È Minusculo :", variavel.islower())
print("Esta capitalizada : ", variavel.istitle())