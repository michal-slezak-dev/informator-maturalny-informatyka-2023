with open("instrukcje.txt", "r") as plik:
    instrukcje = []

    for linia in plik:
        instrukcje.append(linia.split())

tylko_instrukcje = []

for instrukcja in instrukcje:
    tylko_instrukcje.append(instrukcja[0])

instrukcja_licznik = []
for i in range(1, len(tylko_instrukcje)):
    if tylko_instrukcje[i] == tylko_instrukcje[i - 1]:
        counter += 1
    else:
        counter = 1
    instrukcja_licznik.append([tylko_instrukcje[i], counter])

same_ilosci = []
for instrukcja in instrukcja_licznik:
    same_ilosci.append(instrukcja[1])

maxIlosc = max(same_ilosci)

for instrukcja in instrukcja_licznik:
    if instrukcja[1] == maxIlosc:
        maxInstrukcja = instrukcja[0]

print(maxInstrukcja, " ", maxIlosc)

# with open("wyniki4.txt", "a", encoding="UTF-8") as output:
#     output.write("\n\n4.2\n")
#     output.write(str(maxInstrukcja) + " " + str(maxIlosc))