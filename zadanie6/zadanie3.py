def czy_antypalindrom(napis):
    for i in range(int(len(napis)/2)):
        if napis[i] == napis[len(napis) - i - 1]:
            return False
    return True



with open("dane6.txt", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

antypalindromy = []

ile = 0
for napis in napisy:
    if czy_antypalindrom(napis):
        antypalindromy.append(napis)
        print(napis)
        ile += 1
print(ile)

with open("zadanie6_3.txt", "w", encoding="UTF-8") as plikZapis:
    for antypalindrom in antypalindromy:
        plikZapis.write(str(antypalindrom) + "\n")

    plikZapis.write(str(ile))