with open("galerie.txt", "r") as file:
    malls = [line.strip().split()[0] for line in file]

malls_count = {country: malls.count(country) for country in malls}

for country in malls_count:
    print(f"{country} {malls_count[country]}")

with open("wynik4_1.txt", "w", encoding="UTF-8") as out:
    for country in malls_count:
        out.write(f"{country} {malls_count[country]}\n")