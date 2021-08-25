with open("instrukcje.txt", "r") as plik:
    instrukcje = []

    for linia in plik:
        instrukcje.append(linia.split())
     
length = 0
for instrukcja in instrukcje:
    if instrukcja[0] == "DOPISZ":
        length += 1
    elif instrukcja[0] == "USUN":
        length -= 1

print(length)
# with open("wyniki4.txt", "w", encoding="UTF-8") as output:
#     output.write("4.1\n")
#     output.write(str(length))
