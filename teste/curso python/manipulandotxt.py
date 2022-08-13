frase = 'Curso em Video Python'
##vai de 9 ate 21 e vai pulando 2 em 2

print(frase[9:21:2])

#vai de 9 e vai pulando de 3 em 3
print(frase[9::3])


##Analisando str:

#len() pede pra ver o Cumprimento da Frase
print(len(frase))

##count() é usado pra contar quantas letras X tem 
print(frase.count('o'))
# procura quantas letras X tem de 0 a 13 
print(frase.count("o",0,13))

    #find() procura onde ta x coisa
print(frase.find('deo'))
    
    # in ver se tem a palavra x 
print('Curso'in frase)
    
#Transformando string
 
#replace() e usado pra substituir 

print(frase.replace("Python", "Android"))

#upper() usado pra deixar letras mauscula

print(frase.upper())
    
 #lower() usado pra deixar letras minusculas
print(frase.lower()) 
    
#capitalize() ele vaai jogar tudo pra minusculo e deixa do a primera letra MAIUSCULA
print(frase.capitalize())
#title() transforma cada letra da separaçao em maiscula ex: Curso Em Video
print(frase.title())
#strip() ele remove os espaços inuteis no inicio e no fim da str
print(frase.strip())
#rstripe() remove os espaços da direita no caso o ultimo
print(frase.rstrip())
#lstrip() remove os espaços da esquerda no caso os primeiro espaços
print(frase.lstrip()) 
#split() ele refez o index, cada palavra tem uma nova list
print(frase.split())   

# tres aspas serve pra imprimir o texto grande em cada linha que tiver no codigo
print('''blablabla
      oitchau tchau''')