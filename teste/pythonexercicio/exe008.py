from dis import dis


distancia = float(input("Digite uma distancia em metros: "))

km = distancia/1000
hm = distancia/100
dm = distancia/10
cm = distancia*10
dc = distancia*100
mm = distancia*1000

print("A distancia em KM : {}KM".format(km))
print("A distancia em HM : {}HM".format(hm))
print("A distancia em DM : {}DM".format(dm))
print("A distancia em CM : {}CM".format(cm))
print("A distancia em DC : {}DC".format(dc))
print("A distancia em MM : {}MM".format(mm))
