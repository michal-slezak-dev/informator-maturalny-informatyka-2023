from string import ascii_lowercase, ascii_uppercase

with open("szachy.txt", "r") as plik:
    plansze = [[] for _ in range(125)]  # każda lista będzie zawierać wiersze danej planszy

    k = 0
    for linia in plik:
        linia = linia.strip()

        if linia != "":
            plansze[k].append(list(linia))  # jeśli linia nie jest pusta to dodajemy do danej planszy jej wiersz

        else:  # jeśli puste tzn., że zaczyna się kolejna plansza, zwiększamy k o 1 i przechodzimy do następnej linii, w której jest kolejna plansza
            k += 1
            continue

biale_b = list(ascii_uppercase) # zawiera m.in. bierki biale
czarne_b = list(ascii_lowercase) # zawiera m.in bierki czarne

ile = 0 # ilość plansz, na których jest stan równowagi
min_bierek = [] # sumy liczb bierek białych i czarnych podczas stanu równowagi
for plansza in plansze:
    biale, czarne = [], [] # zawierać będą znaki bierek białych i czarnych

    for wiersz in plansza:
        for bierek in wiersz:
            if bierek != ".": # pomijamy puste pola
                if bierek in biale_b:
                    biale.append(bierek)  # dodajemy do listy białe bierki
                else:
                    czarne.append(bierek)  # dodajemy do listy czarne bierki
    biale = list(map(lambda x: x.lower(), biale))  # zamieniamy białe bierki (znaki) na małe (czarne)

    biale_sl = {bierka: biale.count(bierka) for bierka in biale}  # słownik przechowujący w kluczach białe bierki (zamienione na czarne) a w wartościach ilość występowania każdej z nich
    czarne_sl = {bierka: czarne.count(bierka) for bierka in czarne}  # słownik przechowujący w kluczach czarne bierki a w wartościach ilość występowania każdej z nich

    if biale_sl == czarne_sl:  # sprawdzamy czy słowniki się równają (tzn. czy jest stan równowagi)
        ile += 1  # zwiększamy nasz licznik o 1
        min_bierek.append(sum(czarne_sl.values()) + sum(biale_sl.values())) # dodajemy sumę ilości liczb bierek czarnych i białych



print(f"Ilość razy(plansz) w trakcie gry, w której jest równowaga: {ile}")
print(f"Najmniejsza liczba bierek na planszy w stanie równowagi {min(min_bierek)}")


with open("zadanie1_2.txt", "w") as out:
    out.write(f"Ilość razy(plansz) w trakcie gry, w której jest równowaga: {ile}\n")
    out.write(f"Najmniejsza liczba bierek na planszy w stanie równowagi {min(min_bierek)}")