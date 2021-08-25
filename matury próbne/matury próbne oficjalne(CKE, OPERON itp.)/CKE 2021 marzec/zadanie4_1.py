with open("galerie.txt", "r", encoding="UTF-8") as file:
    countries = []

    #Tutaj będziemy do listy countries dodawać kody krajów, oddzielamy każdy wiersz spacją i kod kraju jest na początku, więc indeks ma 0 [0]
    # czyli w liście countries będą wiersze kolejne zapisane jako listy
    for line in file:
        countries.append(line.split(" ")[0])
# print(countries)

number_of_galeries = {}

print("Liczba miast, w których powstaną galerie dla danego kraju: ")
for country in countries:
    number_of_galeries.update({country: countries.count(country)})

for countryCode in number_of_galeries:
    print(f'{countryCode} {number_of_galeries[countryCode]}')

with open("wynik4_1.txt", "w", encoding="UTF-8") as outputFile:
    outputFile.write("ZADANIE 4.1: \n")

    for countryCode in number_of_galeries:
        outputFile.write(f'{countryCode} {number_of_galeries[countryCode]} \n')
