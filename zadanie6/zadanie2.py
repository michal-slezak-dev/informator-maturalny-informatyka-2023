def suma_cyfr(napis):
    suma = 0

    for cyfra in napis:
        suma += int(cyfra)
    return suma

with open("dane6.txt", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

#Ten słownik w kluczach będzie przechowywać podstawę p a w wartościach ilość liczb p-minimalnych
napisy_p_minimalne = {}

#Wypełniamyt słownik podstawami p od 2 do 10 i wartości to puste listy
for i in range(2, 11):
    napisy_p_minimalne.update({i: []})

# Dla każdego napisu w liście szukamy największej cyfry i dodajemy 1, żeby otrzymać podstawę p
# Następnie dla klucza i wartości w słowniku sprawdzami, że jeśli klucz(podstawa p) jest równy tej największej cyfrze + 1 w napisie
# To wtedy dodajemy ten napis do listy, która jest w wartościach słownika
for napis in napisy:
    maxLiczbaSystem = int(max(napis)) + 1

    for klucz, wartosc in napisy_p_minimalne.items():
        if klucz == maxLiczbaSystem:
            napisy_p_minimalne[klucz].append(napis)

# Ta lista potrzebna nam jest do zapisu do pliku
napisy_p_minimalne_max_suma = []

# Dla każdego klucza(podstawy p) w słowniku tworzymy tymczasową listę, która będzie przechowywac nam sumy cyfr danego napisu dla danek podstawy
# Dla każdego napisu w liście z napisami(w wartościach słownika) używamy funkcji suma_cyfr i dodajemy sumę cyfr tego napisu do tymczasowej listy sumy
# Następnie wyłaniamy największą sumę i przypisujemy ją do zmiennej maxSuma
# Następnie dla napisu w liście w wartościach słownika sprawdzamy czy suma cyfr tego napisu jest równa maksymalnej sumie
# Jeśli tak to wypisujemy klucz(podstawę p) i ten napis, dodatkowo do listy napisy_p_minimalne_max_suma dodajemy ten napis
# i robimy break, aby nie szuka już kolejnego
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