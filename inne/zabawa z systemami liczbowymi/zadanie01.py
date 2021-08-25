with open("zadanie01.txt", "r", encoding="UTF-8") as plik:
    wiersze = []

    for wiersz in plik:
        wiersze.append(wiersz.split())
# print(wiersze)

ile = 0
# liczba = "1231321(2)"
# temp = liczba.split("(")
# podstawa = temp[1].replace(")", "")
# print(temp[0])

for wiersz in wiersze:
    temp1 = wiersz[0].split("(")
    podstawa1 = temp1[1].replace(")", "")

    temp2 = wiersz[1].split("(")
    podstawa2 = temp2[1].replace(")", "")

    liczba1 = int(temp1[0], int(podstawa1))
    liczba2 = int(temp2[0], int(podstawa2))

    if liczba1 > liczba2:
        ile += 1

print(f"Wierszy, w których pierwsza liczba jest większa od drugiej jest: {ile}")
