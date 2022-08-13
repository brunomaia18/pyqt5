peso = float(input("Qual o seu peso KG: "))
altura = float(input("Qual a sua altura M: "))
IMC = peso/altura**2

if IMC < 18.5: 
    print("Seu IMC é {:.1f}  você está ABAIXO DO PESO".format(IMC))
elif 18.5 <= IMC < 25:
     print("Seu IMC é {:.1f}  você está com o peso IDEAL".format(IMC))
elif 25 <= IMC < 30:
     print("Seu IMC é {:.1f}  você está SOBREPESO".format(IMC))     
elif 30 <= IMC < 40:
     print("Seu IMC é {:.1f}  você está OBESO".format(IMC))
else:
     print("Seu IMC é {:.1f}  você está com OBESIDADE M".format(IMC))