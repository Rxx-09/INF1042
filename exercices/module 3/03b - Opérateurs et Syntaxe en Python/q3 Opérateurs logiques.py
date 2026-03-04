def verifier_sortie():
    temperature = float(input("Entrez la température : "))
    pluie = input("Pleut-il ? (oui/non) : ").lower()

    if temperature >= 15 and pluie != "oui":
        print("Sortie permise")
    else:
        print("On reste dedans")

verifier_sortie()