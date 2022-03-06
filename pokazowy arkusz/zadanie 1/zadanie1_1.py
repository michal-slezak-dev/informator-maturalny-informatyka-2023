with open("szachy.txt", "r") as plik:
    plansze = [[] for _ in range(125)]

    k = 0
    for linia in plik:
        linia = linia.strip()

        if linia != "":
            plansze[k].append(list(linia)) # jeśli linia nie jest pusta to dodajemy do danej planszy jej wiersz

        else:  # jeśli puste tzn., że zaczyna się kolejna plansza, zwiększamy k o 1 i przechodzimy do następnej linii, w której jest kolejna plansza
            k += 1
            continue


ile = 0  # zlicza ile plansz spełniających waruenk z polecenia
ilosc_kol = []  # ilości pustych kolumn w kolumnach
for plansza in plansze:
    kolumny = [[] for _ in range(8)]  # mamy 8 kolumn

    for i in range(len(plansza)):  # wczytujemy kolumny, odpowiada za poszczegolne kolumny 1, 2, ..., 8
        for j in range(len(plansza)):  # odpowiada za dodawanie poszczegolnych znakow z poszczegolnych wierszy do kolumn
            kolumny[i].append(plansza[j][i])

    puste_kol = 0  # zlicza puste kolumny na planszy
    for kolumna in kolumny:
        if "".join(kolumna) == "........":  # sprawdzamy czy pusta
            puste_kol += 1
    ilosc_kol.append(puste_kol)

    if puste_kol >= 1:
        ile += 1

print(f"Ilość plansz, na których co najmniej 1 kolumna jest pusta: {ile}")
print(f"Największa liczba pustych kolumn na jednej z tych plansz: {max(ilosc_kol)}")

with open("zadanie1_1.txt", "w") as out:
    out.write(f"Ilość plansz, na których co najmniej 1 kolumna jest pusta: {ile}\n")
    out.write(f"Największa liczba pustych kolumn na jednej z tych plansz: {max(ilosc_kol)}")