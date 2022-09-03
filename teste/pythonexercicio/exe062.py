#SUPER P.A


inicio = int(input("Primeiro Termo: "))
razao = int(input("Razão da P.A: "))
termo = inicio
cont = 0
total = 0 
mais = 10
while mais != 0:
      total += mais
      while cont <= total:
            print(f"{termo}", end=' ')
            termo += razao
            cont += 1
      print("pausa")
      mais = int(input("Quantos termos você quer mostrar a mais : "))
print(f"Processo finalizado com sucesso, foi mostrado{total}termos")



     
