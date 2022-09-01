boleano = False
def valores():
  global n1, n2
  n1 = int(input("Digite um valor: "))
  n2 = int(input("Digite outro valor: "))
valores()
while not boleano:
  print("""Escolha uma das opções Abaixo:
  [1] somar
  [2]Multiplicar
  [3]Maior
  [4]Novos numeros
  [5]Sair do programa""")
  pergunta = int(input("Qual é sua opção: "))
  if pergunta == 1:
    soma = n1 + n2
    print(f"A soma entre {n1} e {n2} é {soma}")
  elif pergunta == 2:
    mult = n1* n2
    print(f"A multiplicação entre {n1} e {n2} é {mult}")
  elif pergunta == 3:
    if n1 > n2:
      print(f"O {n1} é maior que o {n2}")
    else:
      print(f"O {n2} é maior que o {n1}")
  elif pergunta == 4:
    valores()
  elif pergunta == 5:
    print("Obrigado por interragir...")
    break

