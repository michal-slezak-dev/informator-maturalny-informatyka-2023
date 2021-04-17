with open("dane6.txt", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())
# print(napisy)

#Ten słownik w kluczach będzie przechowywać podstawę p a w wartościach ilość liczb p-minimalnych
napisy_p_minimalne = {}

#Wypełniamyt słownik podstawami p od 2 do 10 i wartości zerujemy
for i in range(2, 11):
    napisy_p_minimalne.update({i: 0})
# print(napisy_p_minimalne)

# Dla każdego napisu w liście szukamy największej cyfry i dodajemy 1, żeby otrzymać podstawę p
# Następnie dla klucza i wartości w słowniku sprawdzami, że jeśli klucz(podstawa p) jest równy tej największej cyfrze + 1 w napisie
# To wtedy zwiększamy wartość o 1
for napis in napisy:
    maxLiczbaSystem = int(max(napis)) + 1

    for klucz, wartosc in napisy_p_minimalne.items():
        if klucz == maxLiczbaSystem:
            napisy_p_minimalne[klucz] += 1

print("Podstawa p" + " " + "liczba liczb p-minimalnych")
for klucz in napisy_p_minimalne:
    print(klucz, " ", napisy_p_minimalne[klucz])
