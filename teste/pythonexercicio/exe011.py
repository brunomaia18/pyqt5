L = float(input("Digite a Largura da parede : "))
A = float(input("Digite a altura da parede : "))

area = L*A
tinta = round(area/2)

print("Sua parede tem a dimensão de {}x{} e a area de {}m²".format(L,A,area))
print("para pintar essa parede você precisa de {}L de tintas".format(tinta))