n1 = float(input("Digite sua primeira nota : "))
n2 = float(input("digite sua segunda nota : "))

media = (n1+n2)/ 2

if media >= 7 :
    print("sua media foi {} você foi aprovado".format(media))
elif media <= 6.9 and media >= 5.0: # 7 > media >= 5
    print("sua media foi {} você está de recuperação ".format(media))
elif media < 4.9:
    print ("sua media foi {} você foi REPROVADO ")
    