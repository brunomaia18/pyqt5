import sys
from tkinter import mainloop
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton

class janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira janela"
        #PARA CRIAR UM BOTAO#####################
        botao1 =QPushButton("BOTÃO 1 ", self)
        botao1.move(250, 150)
        botao1.resize(150,50)
        botao1.setStyleSheet("QPushButton {background-color: #0FB328; font: normal 18pt Arial}")
        botao1.clicked.connect(self.botao1_click)
       ###########################################
        self.CarregarJanela()

    def CarregarJanela(self):    
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    def botao1_click(self):
        print("O Botão foi clicado ")   
aplicacao = QApplication(sys.argv)
j = janela()        
sys.exit(aplicacao.exec())
