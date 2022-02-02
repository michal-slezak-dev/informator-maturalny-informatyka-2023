from collections import deque

# do listy cities dodajemy listę z miastem oraz wymiarami lokali, bez kodu kraju, bo nie jest potrzebyn
with open("galerie.txt", "r") as file:
    cities = []
    for line in file:
        city_and_measure = []
        line = line.strip().split()
        city = line[1] # tylko miasto

        # zamieniamy najpierw same wymiary na liczby całkowite, używając funkcji map()
        city_and_measure = deque(list(map(int, line[2:]))) # dzięki tek mozna na poczatek dodać element

        city_and_measure.appendleft(city) # dodajemy na początek miasto
        cities.append(list(city_and_measure))

# słownik, który w kluczach przechowuje miasto a w wartościach listę z powierzchniami lokali
city_and_areas = dict()
for city in cities:
    areas = []

    for i in range(2, len(city), 2):
        if city[i] != 0:
            areas.append(city[i - 1] * city[i])

    city_and_areas.update({city[0]: sorted(areas)})

# słownik, który w kluczach przechowuje miasto a w wartościach liczbę lokali różnego typu
city_and_num_of_different_places = dict()
for city in city_and_areas:
    num_of_different_places = 1
    list_of_areas = city_and_areas[city]

    for i in range(1, len(list_of_areas)):
        if list_of_areas[i] != list_of_areas[i - 1]:
            num_of_different_places += 1

    city_and_num_of_different_places.update({city: num_of_different_places})

# wyłaniamy max i min liczbę lokali różnego typu
max_num_of_different_places = max(city_and_num_of_different_places.values())
min_num_of_different_places = min(city_and_num_of_different_places.values())

# wyznaczamy miasta, w których jest najwięcej i najmniej lokali różnego typu
for city in city_and_num_of_different_places:
    if city_and_num_of_different_places[city] == max_num_of_different_places:
        max_city = city

    if city_and_num_of_different_places[city] == min_num_of_different_places:
        min_city = city

print(f"{max_city} {max_num_of_different_places}")
print(f"{min_city} {min_num_of_different_places}")

with open("wynik4_3.txt", "w", encoding="UTF-8") as out:
    out.write(f"{max_city} {max_num_of_different_places}\n")
    out.write(f"{min_city} {min_num_of_different_places}")