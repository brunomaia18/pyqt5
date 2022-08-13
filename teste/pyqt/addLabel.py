import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class janela (QMainWindow):
    ##Criando uma funçao PRINCIOPAL, DIZENDO O QUE TEM EM CADA COISA
    def __init__(self):
        super().__init__()

        self.topp = 100
        self.esquerda = 100 
        self.largura = 800
        self.altura = 600
        self.titulo = "Segunda Janela"
        ##TEM QUE CHAMAR A FUNÇAO CarregarJanela
        self.CarregarJanela()
    ##FAZENDO A JANELA SE FORMAR
    def CarregarJanela(self):
        #fazendo a largura, altura e onde a janela se posisionara na tela da pessoa    
        self.setGeometry(self.esquerda, self.topp, self.largura,self.altura)
        #Botando o titulo da janela
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = janela()
sys.exit(aplicacao.exec())
