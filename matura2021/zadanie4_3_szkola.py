with open("instrukcje.txt", "r") as plik:
    literki = []

    for linia in plik:
        if linia.split()[0] == "DOPISZ":
            literki.append(linia.split()[1])

literki_ilosc = dict()

for literka in literki:
    literki_ilosc.update({literka: literki.count(literka)})

maxIlosc = max(literki_ilosc.values())

for literka in literki_ilosc:
    if literki_ilosc[literka] == maxIlosc:
        maxLiterka = literka

print(maxLiterka, " ", maxIlosc)

# with open("wyniki4.txt", "a", encoding="UTF-8") as output:
#     output.write("\n\n4.3\n")
#     output.write(str(maxLiterka) + " " + str(maxIlosc))