with open("zadanie02.txt", "r", encoding="UTF-8") as plik:
    wiersze = []

    for wiersz in plik:
        wiersze.append(wiersz.split())
# print(wiersze)

ile = 0

literki = ["A", 10, "B", 11, "C", 12, "D", 13, "E", 14, "F", 15]

hexadecimal = dict()
for i in range(0, 11, 2):
    hexadecimal[literki[i]] = literki[i + 1]

for wiersz in wiersze:
    temp1 = wiersz[0].split("(")
    podstawa1 = temp1[1].replace(")", "")

    temp2 = wiersz[1].split("(")
    podstawa2 = temp2[1].replace(")", "")

    maxLiczba1 = max(temp1[0]).upper()
    maxLiczba2 = max(temp2[0]).upper()

    if maxLiczba1 in list(hexadecimal.keys()):
        maxLiczba1 = hexadecimal[maxLiczba1]

    if maxLiczba2 in list(hexadecimal.keys()):
        maxLiczba2 = hexadecimal[maxLiczba2]

    sprawdzanaPodstawa1 = int(maxLiczba1)
    sprawdzanaPodstawa2 = int(maxLiczba2)

    if sprawdzanaPodstawa1 >= int(podstawa1) or sprawdzanaPodstawa2 >= int(podstawa2):
        ile += 1

print(f"Wierszy, w których wystąpiły opisane w poleceniu błędy jest: {ile}")
