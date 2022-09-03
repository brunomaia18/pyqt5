#Termos de uma PA 2.0



print('''Gerador de PA
      =>=>=>=>=>=>=>=>=>=>''')
inicio = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a Razão da sua PA: "))
cont = 1 

while cont <= 10:
      print(f"{inicio}", end= ' ')
      inicio += razao
      cont+= 1
print ("---FIM---")    
