def get_max(list):
    max_element = list[0]
    for element in list:
        if element > max_element:
            max_element = element

    return max_element


def get_min(list):
    min_element = list[0]
    for element in list:
        if element < min_element:
            min_element = element

    return min_element

# do listy cities dodajemy listę z miastem oraz wymiarami lokali, usuwamy też kod kraju, bo nie jest potrzebyn
with open("galerie.txt", "r") as file:
    cities = []
    for line in file:
        line = line.strip().split()
        line.pop(0)
        cities.append(line)

# zamiana wymiarów lokali z danego miasta na liczby całkowite
for city in cities:
    for i in range(1, len(city)):
        city[i] = int(city[i])

# słownik, który przechowuje w kluczach miasto a w wartościach tuple z powierzchnią całkowitą i liczbą lokali
cities_mall_area_and_num_of_places = dict()
for city in cities:
    area_of_the_mall = 0 # powierzchnia całkowita galerii
    num_of_places = 0 # liczba lokali w danej galerii

    # dodajemy powierzchnie kolejnych lokali
    for i in range(2, len(city), 2):
        area_of_the_mall += (city[i - 1] * city[i])

    # zwiększamy liczbę lokali, pomijając 0
    for i in range(1, len(city), 2):
        if city[i] != 0:
            num_of_places += 1

    cities_mall_area_and_num_of_places.update({city[0]: (area_of_the_mall, num_of_places)})

# ta lista przechowuje same powierzchnie całkowite galerii
only_areas = []
for city in cities_mall_area_and_num_of_places:
    only_areas.append(cities_mall_area_and_num_of_places[city][0])

max_area = get_max(only_areas) # największa powierzchnia
min_area = get_min(only_areas) # najmniejsza powierzchnia

# wyznaczamy miasto z najmniejszą i największą powierzchnią galerii
for city in cities_mall_area_and_num_of_places:
    if cities_mall_area_and_num_of_places[city][0] == max_area:
        max_city = city

    if cities_mall_area_and_num_of_places[city][0] == min_area:
        min_city = city

# wypisanie odpowiedzi do podpunktu a)
print(f"a)\n")

# przechowuje nam stringi miasto powierzchnia liczba_lokali
output = []
for city in cities_mall_area_and_num_of_places:
    mall_area = cities_mall_area_and_num_of_places[city][0]
    num_of_places = cities_mall_area_and_num_of_places[city][1]

    print(f"{city} {mall_area} {num_of_places}")
    output.append(f"{city} {mall_area} {num_of_places}")

# wypisanie odpowiedzi do podpunktu b)
print(f"\nb) {max_city} {max_area}\n{min_city} {min_area}")

# zapis do pliku z odpowiedziami
with open("wynik4_2a.txt", "w", encoding="UTF-8") as out:
    for city in output:
        out.write(f"{city}\n")

with open("wynik4_2b.txt", "w", encoding="UTF-8") as out:
    out.write(f"{max_city} {max_area}\n{min_city} {min_area}")