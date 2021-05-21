import string
with open("instrukcje.txt", "r") as plik:
    instrukcje = []

    for linia in plik:
        instrukcje.append(linia.split())

literki = list(string.ascii_uppercase)
literki.append("A")

zamiana = dict()

for i in range(1, len(literki)):
    zamiana[literki[i - 1]] = literki[i]

napis = []
for instrukcja in instrukcje:
    if instrukcja[0] == "DOPISZ":
        napis.append(instrukcja[1])
    elif instrukcja[0] == "ZMIEN":
        napis[-1] = instrukcja[1]
    elif instrukcja[0] == "USUN":
        napis.pop(-1)
    elif instrukcja[0] == "PRZESUN":
        if instrukcja[1] in napis:
            for i in napis:
                if i == instrukcja[1]:
                    napis[napis.index(i)] = zamiana[i]
                    break
print("".join(napis))

# with open("wyniki4.txt", "a", encoding="UTF-8") as output:
#     output.write("\n\n4.4\n")
#     output.write("".join(napis))