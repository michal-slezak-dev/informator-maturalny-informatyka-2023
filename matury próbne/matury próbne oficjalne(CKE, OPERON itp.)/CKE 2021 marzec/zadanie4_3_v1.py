def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

    return list

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

def get_dict_values(dict):
    values = []
    for key in dict:
        values.append(dict[key])

    return values

with open("galerie.txt", "r") as file:
    cities = []
    for line in file:
        line = line.strip().split()
        line.pop(0)

        cities.append(line)

# zamiana wymiarów na liczby całkowite
for city in cities:
    for i in range(1, len(city)):
        city[i] = int(city[i])

# słownik, który w kluczach przechowuje miasto a w wartościach listę z powierzchniami lokali
city_and_areas = dict()
for city in cities:
    areas = []

    for i in range(2, len(city), 2):
        if city[i] != 0:
            areas.append(city[i - 1] * city[i])

    city_and_areas.update({city[0]: bubble_sort(areas)})

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
max_num_of_different_places = get_max(get_dict_values(city_and_num_of_different_places))
min_num_of_different_places = get_min(get_dict_values(city_and_num_of_different_places))

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