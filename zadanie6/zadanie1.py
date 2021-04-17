with open("dane6.txt", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())
# print(napisy)

napisy_p_minimalne = {}

for i in range(2, 11):
    napisy_p_minimalne.update({i: 0})
# print(napisy_p_minimalne)

for napis in napisy:
    maxLiczbaSystem = int(max(napis)) + 1

    for klucz, wartosc in napisy_p_minimalne.items():
        if klucz == maxLiczbaSystem:
            napisy_p_minimalne[klucz] += 1

print("Podstawa p" + " " + "liczba liczb p-minimalnych")
for klucz in napisy_p_minimalne:
    print(klucz, " ", napisy_p_minimalne[klucz])
