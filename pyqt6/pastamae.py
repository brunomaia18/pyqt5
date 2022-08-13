
import login
from dade import cadastro_usuario, criar_banco, entrar_usario


def verificando():

    nome = login.le.text()
    senha = login.le2.text()
    if nome and senha:
        if entrar_usario():
            login.informando.setText("acesso permitido")
        elif nome == "admin" and senha == "12345":
            login.informando.setText("pagina Adm")
        else: 
            login.informando.setText('acesso negado')
def cadastrar():
    nome = login.le.text()
    senha = login.le2.text()
    if nome and senha:
        if cadastro_usuario():
            login.informando.setText("CADASTRADO")
        else: 
            login.informando.setText("Cadastro invalido")



def painel_user():
    login.janela.resize(400,300)
    login.janela.setWindowTitle("Login")
    login.janela.setStyleSheet("background:gray")

    login.btn.setGeometry(70,200,80,20)
    login.btn.clicked.connect(verificando)

    login.botao2.setGeometry(230,200,80,20)
    login.botao2.clicked.connect(cadastrar)

    login.label.move(70,100)
    login.label2.move(68,130)
    login.informando.move(70,240)
    login.informando.resize(200,80)

    login.le.setGeometry(130,100,150,20)
    login.le2.setGeometry(130,130,150,20)
    login.le2.setEchoMode(login.QLineEdit.EchoMode.Password)
    login.janela.show()
    
        

    login.app.exec()


painel_user()