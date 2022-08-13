import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel





app = QApplication(sys.argv)
janela = QWidget()
btn = QPushButton("ok", janela)
botao2 = QPushButton("cadastrar",janela)
label = QLabel("Users:", janela)
label2 = QLabel("Senha:", janela)
informando=QLabel("",janela)
le = QLineEdit("", janela)
le2 = QLineEdit("", janela)
nome = le.text()
senha =le2.text()



