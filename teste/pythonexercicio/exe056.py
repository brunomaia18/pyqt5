from smtpd import MailmanProxy
from ssl import HAS_NEVER_CHECK_COMMON_NAME
from turtle import home


s = 0
maisvelho = ""
maior = 0 
somamulher = 0

for i in range(1,5):
    print(f"------{i} PESSOA------")
    Nome = str(input("Nome: ")).strip()
    idade = float(input("IDADE: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    s += idade
    media = float(s/4)


    if sexo == 'F' and idade < 20:
        somamulher+=1


    if i == 1 and sexo == "M":
        maior = idade
        maisvelho = Nome
    else:
        if maior < idade and sexo == "M":
            maior = idade
            maisvelho = Nome
            
      

print(f"A media das idades foi {media}")
print(f"O Homem mais velho tem {maior} e o nome é {maisvelho}")
print(f"tem {somamulher} mulheres com menos de 20 anos")