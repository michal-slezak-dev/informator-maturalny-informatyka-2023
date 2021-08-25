with open("galerie.txt", "r", encoding="UTF-8") as file:
    galleries_info = []

    # Tutaj będziemy do listy countries dodawać kody krajów, oddzielamy każdy wiersz spacją i kod kraju jest na początku, więc indeks ma 0 [0]
    # czyli w liście countries będą wiersze kolejne zapisane jako listy
    for line in file:
        galleries_info.append(line.strip("\n").split(" "))
# print(galleries_info)

# Tworzymy słownik, w którym będą przechowywane miasta i listy z powierzchniami ich galerii
cityAndGalleriesArea = {}

# W pętli tworzymy listę, do której będziemy dodawać aktualne poewierzchnie danych galerii w danym mieście
# Wytłumaczenie dot. warunków pętli for i in range() jest w zadaniu4_2.py
# deklarujemy zmienną currentArea, do której przypisujemy powierzchnię danej galerii, potem do tymczasowej listy areas dodajemy powierzchnie danych galerii danego miasta
# Na koniec do słownika dodajemy nazwę miasta i powierzchnie galerii, które mają byćw tym mieście
for gallery in galleries_info:
    areas = [] # Tworzymy listę, która będzie przechowywać aktualne powierzchnie danych galerii
    for i in range(2, len(gallery) - 1, 2):
        if gallery[i] != 0:
            currentArea = int(gallery[i]) * int(gallery[i + 1])
            areas.append(currentArea)
            cityAndGalleriesArea.update({gallery[1]: areas})
# print(cityAndGaleriesArea)

# Tutaj w wartościach, które są listami filtrujemy jes tak, żeby w liście przechowującej wartości nie było powierzchni = 0 + sortujemy powierzchnię
# Używamy tego funkcji filter() oraz funkcji anonimowej lambda, która sprawdza czy cos nie jest zerem
# Jeśli nie jest to zwraca true, w przeciwnym wypadku false
for city in cityAndGalleriesArea:
    cityAndGalleriesArea[city] = sorted(list(filter(lambda x: x != 0, cityAndGalleriesArea[city])))
# print(cityAndGaleriesArea)

# Tworzymy słownik, w którym będziemy przechowywać nazwę miast i liczbę galerii tego samego rodzaju
citiesWithDifferentTypeOfShops = {}

# W tej pętli zliczamy lokale różnego typu
# Wewnętrzna pętla zaczyna się od 0, ponieważ porównujemy też powierzchnię lokalu pierwszego z tą lokalu ostatniego, więc porównujemy też
# powierzchnię o indeksie 0 z tą o indeksie -1 (indeksowanie ujemne w pythonie ułatwia życie czasami :_))
# Jeśli powierzchnię są różne to zwiększamy licznik differentType o 1 i na końcu dodajemy do słownika citiesWithDifferentTypeOfShops miasto i liczbę lokali różnego typu
for city in cityAndGalleriesArea:
    shopAreas = cityAndGalleriesArea[city]
    differentType = 0
    for i in range(0, len(shopAreas)):
        if shopAreas[i] != shopAreas[i - 1]:
            differentType += 1
    citiesWithDifferentTypeOfShops.update({city: differentType})
# print(citiesWithDifferentTypeOfShops)

# Wyłaniamy największą i najmniejszą liczbę lokali różnego typu
maxShopsOfDifferentType = max(citiesWithDifferentTypeOfShops.values())
minShopsOfDifferentType = min(citiesWithDifferentTypeOfShops.values())
# print(maxShopsOfDifferentType)
# print(minShopsOfDifferentType)

# Tutaj wyłaniamy miasta z największą i najmniejszą liczbą lokali różnego typu
for city in citiesWithDifferentTypeOfShops:
    if citiesWithDifferentTypeOfShops[city] == maxShopsOfDifferentType:
        maxCityWithDifferentType = city
    if citiesWithDifferentTypeOfShops[city] == minShopsOfDifferentType:
        minCityWithDifferentType = city

print(f'Miasto o największej liczbie lokali różnego typu i liczba lokali różnego typu: {maxCityWithDifferentType} {maxShopsOfDifferentType}')
print(f'Miasto o najmniejszej liczbie lokali różnego typu i liczba lokali różnego typu: {minCityWithDifferentType} {minShopsOfDifferentType}')

with open("wynik4_3.txt", "w", encoding="UTF-8") as outputFile:
    outputFile.write("ZADANIE 4.3\n")
    outputFile.write(f'Miasto o największej liczbie lokali różnego typu i liczba lokali różnego typu: {maxCityWithDifferentType} {maxShopsOfDifferentType}\n')
    outputFile.write(f'Miasto o najmniejszej liczbie lokali różnego typu i liczba lokali różnego typu: {minCityWithDifferentType} {minShopsOfDifferentType}')
