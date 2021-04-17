def suma_cyfr(napis):
    suma = 0

    for cyfra in napis:
        suma += int(cyfra)
    return suma

with open("dane6.txt", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

napisy_p_minimalne = {}

for i in range(2, 11):
    napisy_p_minimalne.update({i: []})

for napis in napisy:
    maxLiczbaSystem = int(max(napis)) + 1

    for klucz, wartosc in napisy_p_minimalne.items():
        if klucz == maxLiczbaSystem:
            napisy_p_minimalne[klucz].append(napis)

napisy_p_minimalne_max_suma = []

print("Podstawa p" + "      liczba p-minimalna o największej sumie cyfr")
for klucz in napisy_p_minimalne:
    sumy = []
    for napis in napisy_p_minimalne[klucz]:
        sumy.append(suma_cyfr(napis))

    maxSuma = max(sumy)
    for napis in napisy_p_minimalne[klucz]:
        if suma_cyfr(napis) == maxSuma:
            print(klucz, "           ", napis)
            napisy_p_minimalne_max_suma.append(napis)
            break

with open("zadanie6_2.txt", "w", encoding="UTF-8") as plikZapis:
    plikZapis.write("Podstawa p " + "     liczba p-minimalna o największej sumie cyfr\n")
    p = 2

    for napisPMinimalny in napisy_p_minimalne_max_suma:
        plikZapis.write(str(p) + "           " + napisPMinimalny + "\n")
        p += 1