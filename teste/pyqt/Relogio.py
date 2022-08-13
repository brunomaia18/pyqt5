from cProfile import label
from cgitb import text
from datetime import datetime
from datetime import time
from tkinter import *

#####BASE PARA CRIAR UM JANELA######
janela = Tk()
janela.title("Horas")#titulo da janela
janela.geometry("440x180")#area da janela
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg="White")

def relogio():
############# VARIAVEL HORA ###############
    tempo= datetime.now()
    horas = tempo.strftime("%H:%M:%S")
    l1.config(text=horas)
    l1.after(200, relogio) ## quando passa x milesegundos ele volta pra funçao e atualiza a hora
##############IMPRIMIR NO tKINTER#################################

l1 = Label(janela, text="", font=("Arial 80"))
l1.grid(row=0, column=0, sticky=NW, padx=5) #usar a medida do que vai aparecer 
relogio() #chama a funçao hora 
janela.mainloop()#faz a janela aparecer