with open("szachy.txt", "r") as plik:
    plansze = [[] for _ in range(125)]

    k = 0
    for linia in plik:
        linia = linia.strip()

        if linia != "":
            plansze[k].append(list(linia))  # jeśli linia nie jest pusta to dodajemy do danej planszy jej wiersz

        else:  # jeśli puste tzn., że zaczyna się kolejna plansza, zwiększamy k o 1 i przechodzimy do następnej linii, w której jest kolejna plansza
            k += 1
            continue

b_wieza = cz_wieza = 0
for plansza in plansze:
    kolumny = [[] for _ in range(8)]  # mamy 8 kolumn

    for i in range(len(plansza)):  # wczytujemy kolumny, odpowiada za poszczegolne kolumny 1, 2, ..., 8
        for j in range(len(plansza)):  # odpowiada za dodawanie poszczegolnych znakow z poszczegolnych wierszy do kolumn
            kolumny[i].append(plansza[j][i])

    # sprawdzamy wiersze:
    for wiersz in plansza:
        # wieża biała i czarny król:
        if "W" in wiersz and "k" in wiersz:
            biala_indx = wiersz.index("W")  # szukamy indeksu wieży
            czarny_indx = wiersz.index("k")  # szukamy indeksu króla

            if biala_indx > czarny_indx:  # biała wieża jest po czarnym królu
                pomiedzy = list(set(wiersz[czarny_indx + 1:biala_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ['.'] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                        b_wieza += 1
            elif biala_indx < czarny_indx:  # biała wieża jest przed czarnym królem
                pomiedzy = list(set(wiersz[biala_indx + 1:czarny_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ["."] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    b_wieza += 1

        # wieża czarna i bialy król:
        if "w" in wiersz and "K" in wiersz:
            czarna_indx = wiersz.index("w")  # szukamy indeksu wieży
            bialy_indx = wiersz.index("K")  # szukamy indeksu króla

            if czarna_indx > bialy_indx:  # czarna wieża jest po białym królu
                pomiedzy = list(set(wiersz[bialy_indx + 1:czarna_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ['.'] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    cz_wieza += 1
            elif czarna_indx < bialy_indx: # czarna wieża jest przed królem
                pomiedzy = list(set(wiersz[czarna_indx + 1:bialy_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ["."] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    cz_wieza += 1

    # sprawdzamy kolumny:
    for kolumna in kolumny:
        # wieża biała i czarny król:
        if "W" in kolumna and "k" in kolumna:
            biala_indx = kolumna.index("W")  # szukamy indeksu wieży
            czarny_indx = kolumna.index("k")  # szukamy indeksu króla

            if biala_indx > czarny_indx:  # biała wieża po czarnym królu
                pomiedzy = list(set(kolumna[czarny_indx + 1:biala_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ['.'] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    b_wieza += 1
            elif biala_indx < czarny_indx:  # biała wieża przed czarnym królem
                pomiedzy = list(set(kolumna[biala_indx + 1:czarny_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ["."] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    b_wieza += 1

        # wieża czarna i bialy król:
        if "w" in kolumna and "K" in kolumna:
            czarna_indx = kolumna.index("w")  # szukamy indeksu wieży
            bialy_indx = kolumna.index("K")  # szukamy indeksu króla

            if czarna_indx > bialy_indx:
                pomiedzy = list(set(kolumna[bialy_indx + 1:czarna_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ['.'] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    cz_wieza += 1
            elif czarna_indx < bialy_indx:
                pomiedzy = list(set(kolumna[czarna_indx + 1:bialy_indx]))  # lista składająca się ze znaków pomiędzy wieżą a królem
                if pomiedzy == ["."] or pomiedzy == []:  # sprawdzamy czy nie ma żadnych innych bierek pomiędzy królem a wieżą
                    cz_wieza += 1

print(f"Biała wieża szachuje czarnego króla {b_wieza} razy.")
print(f"Czarna wieża szachuje białego króla {cz_wieza} raz.")

with open("zadanie1_3.txt", "w") as out:
    out.write(f"Biała wieża szachuje czarnego króla {b_wieza} razy.\n")
    out.write(f"Czarna wieża szachuje białego króla {cz_wieza} raz.")
