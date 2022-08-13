import sqlite3 
import login as test

global cursor
global data
global acesso

def criar_banco():
    global data
    global cursor
    
    data = sqlite3.connect("data_base.db")
    cursor = data.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(nome text, senha text)")

def cadastro_usuario():
    criar_banco()
    
    acesso =False
    nome = test.le.text()
    senha = test.le2.text()
    if nome and senha:
        try:
            cursor.execute("INSERT INTO users VALUES('{}','{}')".format(nome,senha))
            data.commit()
            data.close()
        except:
            acesso = False
    else:
        acesso =False
        
    return acesso

def entrar_usario():
    criar_banco()
    
    acesso = False
    nome = test.le.text()
    senha = test.le2.text()
    if nome and senha:
        try:
            cursor.execute("SELECT senha FROM users WHERE nome = '{}'".format(nome))
            senha_cap = cursor.fetchall()
            if senha == senha_cap[0][0]:
                acesso = True
            else:
                acesso = False
        except:
            acesso = False
    return acesso
    
            