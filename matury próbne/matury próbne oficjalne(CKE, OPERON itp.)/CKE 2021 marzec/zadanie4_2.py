with open("galerie.txt", "r", encoding="UTF-8") as file:
    galleries_info = []

    # Tutaj będziemy do listy countries dodawać kody krajów, oddzielamy każdy wiersz spacją i kod kraju jest na początku, więc indeks ma 0 [0]
    # czyli w liście countries będą wiersze kolejne zapisane jako listy
    for line in file:
        galleries_info.append(line.strip("\n").split(" "))
# print(galleries_info)

# W tej pętli dla każdego wiersza deklarujemy 2 zmienne - 1. to ta z sumą powierzchni lokali 2. to ta, która będzie liczyć ilość lokali
# pętlę wewnętrzną zaczynamy od 2, ponieważ gallery[0] i gallery[1] to kod kraju i nazwa miasta, których niue potrzebujemy na ten moment
# krok pętli jest ustawiony na 2, ponieważ jak mamy 4 wymiary to pętla leci tak: np. >1 2-->3 4-->5 6-->7 8 potem do sumOfGallery dodaje iloczyn gallery[i] i gallery[i + 1], czyli
# jak mamy właśnie >1 2-->3 4-->5 6-->7 8 to dodaje najpierw robi areaOfGallery += 1 * 2 --> areaOfGallery += 3 * 4 --> areaOfGallery += 5 * 6 --> areaOfGallery += 7 * 8
# jeżeli któryś z wymiarów danego lokalu jest różny od zera to zwiększamy numberOfShops o 1, bo krok jest co 2, więc każde 2 wymiary to 1 lokal
# na koniec wypisujemy miasto, powierzchnię galerii i liczba lokali w tej galerii

# Tworzymy słownik, która będzie przechowywać w sobie kolejne listy z miastem i z powierzchnią galerii
cityAndAreaOfGalleries = {}

# Tworzymy listę, do której zapiszemy miasto, powierzchnię i liczbę lokali
cityAreaAndShops = []

print("a)")
for gallery in galleries_info:
    areaOfGallery = 0
    numberOfShops = 0
    for i in range(2, len(gallery) - 1, 2):
        areaOfGallery += (int(gallery[i]) * int(gallery[i + 1])) # dodajemy powierzchnię galerii
        if int(gallery[i]) != 0:
            numberOfShops += 1      #liczba galerii

    cityAndAreaOfGalleries.update({gallery[1]: areaOfGallery}) # dodajemy do słownika cityAndSumOfGaleries miasto i powierzchnię całkowitą galerii
    cityAreaAndNumberOfShops = str(gallery[1]) + " " + str(areaOfGallery) + " " + str(numberOfShops) # ta zmienna potrzebna jest też do zapisania wyników do pliku
    cityAreaAndShops.append(cityAreaAndNumberOfShops)

    print(cityAreaAndNumberOfShops)
    # print(f'{gallery[1]} {areaOfGallery} {numberOfShops}') # wypisujemy miasto, powierzchnię całkowitą galerii i liczbę lokali
# print(cityAndSumOfGaleries)

# Wyznaczamy największą i najmniejszą powierzchnię galerii
maxAreaGallery = max(cityAndAreaOfGalleries.values())
minAreaGallery =  min(cityAndAreaOfGalleries.values())
# print(maxAreaGallery)
# print(minAreaGallrey)

# Wyznaczamy miasto dla największej i najmniejszej powierzchni galerii
for city in cityAndAreaOfGalleries:
    if cityAndAreaOfGalleries[city] == maxAreaGallery:
        maxAreaCity = city
    if cityAndAreaOfGalleries[city] == minAreaGallery:
        minAreaCity = city

print("\nb)")
print(f'Miasto z galerią o największej powierzchni  oraz powierzchnia tej galerii: {maxAreaCity} {maxAreaGallery}')
print(f'Miasto z galerią o najmniejszej powierzchni oraz powierzchnia tej galerii: {minAreaCity} {minAreaGallery}')

### ZAPIS DO PLIKU ###
with open("wynik4_2a.txt", "w", encoding="UTF-8") as outputFile:
    outputFile.write("ZADANIE 4_2 \n")
    outputFile.write("a) \n")
    for info in cityAreaAndShops:
        outputFile.write(f'{info} \n')

with open("wynik4_2b.txt", "w", encoding="UTF-8") as outputFile2:
    outputFile2.write("ZADANIE 4_2 \n")
    outputFile2.write("b) \n")

    outputFile2.write(f'Miasto z galerią o największej powierzchni oraz powierzchnia tej galerii: {maxAreaCity} {maxAreaGallery}\n')
    outputFile2.write(f'Miasto z galerią o najmniejszej powierzchni oraz powierzchnia tej galerii: {minAreaCity} {minAreaGallery}')
