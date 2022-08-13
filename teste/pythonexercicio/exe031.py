distancia = int(input("Digite a distancia que você vai pecorrer: "))



if distancia <= 200 : 
    preço = distancia * 0,50
    
else:
    preço = distancia  * 0,45
  
    
    
print("voce ira gastar R${}".format(preço))