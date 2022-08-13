casa = int(input("Qual o valor da casa que você quer : "))
salario = int(input("Qual o seu salario mensal : "))
anos =int(input("Quantos anos você quer pagar a casa : "))

meses = (12*anos)/1

max_pagar = ((salario *  30/100)- salario) + salario
parcela = casa / meses

if parcela <= max_pagar :
    print("Parabens você pode comprar essa casa")
elif parcela > max_pagar: 
    print("Sinto muito você nao pode comprar esssa casa, veja uma com um valor menor ou tente aumentar o tempo de pagamento")  
else:
    print('legal')  