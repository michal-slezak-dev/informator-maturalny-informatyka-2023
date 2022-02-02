def get_count(list, target):
    counter = 0
    for element in list:
        if element == target:
            counter += 1

    return counter

def get_countries_and_num_of_malls(list):
    countries_malls_count = dict()

    for country in list:
        countries_malls_count.update({country: get_count(list, country)})

    return countries_malls_count

with open("galerie.txt", "r") as file:
    malls = []
    for line in file:
        line = line.strip().split()
        malls.append(line[0])

malls_count = get_countries_and_num_of_malls(malls)
for country in malls_count:
    print(f"{country} {malls_count[country]}")

with open("wynik4_1.txt", "w", encoding="UTF-8") as out:
    for country in malls_count:
        out.write(f"{country} {malls_count[country]}\n")