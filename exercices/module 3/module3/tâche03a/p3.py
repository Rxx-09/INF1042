nombre = float(input("Entrez un nombre : "))

carre = pow(nombre, 2)
carre_arrondi = round(carre, 2)

print("Le carré est :", carre_arrondi)

for i in range(1, 6):
    print(i)