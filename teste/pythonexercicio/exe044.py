print("---"*10)
print("        DOCERIA NOANDA      ")
print("---"*10)

valor= float(input("Digite o valor a pagar R$ "))

print('''Qual o metodo de ṕagamento ?
      [1] á vista
      [2] à vista no cartão
      [3] 2X sem juros
      [4] parcelar no cartão ''')
metodopagamento = int(input("ESCOLHA UM METODO DE PAGAMENTO: "))

avista = valor - (valor * 10/100)

avistacartao = valor - (valor * 5/100)

semjuros = valor/2

parcelas = valor + (valor * 20/100)

if metodopagamento == 1 : 
    print("Sua compra de R${} vai custar R${} no final".format(valor,avista))
elif metodopagamento == 2:
    print("Sua compra de R${} vai custar R${} no final".format(valor,avistacartao))
elif metodopagamento == 3: 
    print("sua compra de R${} vai ficar 2 parcelas de {}".format(valor, parcelas))
elif metodopagamento == 4:
    
    nparcelas = int(input("Em quantas parcelas você quer pagar : "))
    formula = parcelas/nparcelas
    print('você ira pagar {}X de R${}'.format(nparcelas,formula))
    print ("Sua compra de R${} ficará R${}".format(valor, parcelas))
else:
    print("ERRO!!!! Tente novamente")