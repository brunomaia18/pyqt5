from time import sleep
import pywhatkit as pk
import pandas
import keyboard as kb

df = pandas.read_excel("automatico.xlsx")

print(df)

for i, mensagem in enumerate(df["Mensagem"]):
    
    numero = df.loc[i,"Numero"]
    pk.sendwhatmsg_instantly(numero,mensagem)
    sleep(3)