with open("galerie.txt", "r") as file:
    malls = []
    for line in file:
        line = line.strip().split()
        malls.append(line[0])

malls_count = dict()
for country in malls:
    malls_count.update({country: malls.count(country)})

for country in malls_count:
    print(f"{country} {malls_count[country]}")

with open("wynik4_1.txt", "w", encoding="UTF-8") as out:
    for country in malls_count:
        out.write(f"{country} {malls_count[country]}\n")