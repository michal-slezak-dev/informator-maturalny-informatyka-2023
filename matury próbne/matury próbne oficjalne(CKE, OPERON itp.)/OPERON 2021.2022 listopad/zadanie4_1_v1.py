def get_max(list):
    max_current = -12312

    for element in list:
        if element > max_current:
            max_current = element

    return max_current

def pow(num, base):
    res = 1

    while base > 0:
        res *= num
        base -= 1

    return res

def get_count(list, target):
    counter = 0

    for element in list:
        if element == target:
            counter += 1

    return counter

def get_values_dict(dict):
    values = []
    for key in dict:
        values.append(dict[key])

    return values

def squared(num): # 7 --> 49 | 49 --> 4^2 + 9^2 ->97
    res = 0
    for digit in str(num):
        res += pow(int(digit), 2)

    return res

def is_happy(num):
    """
    Najpierw do zmiennej current przypisujemy sumę kwadratów pierwotnej liczby, następnie dodajemy taką sumę do listy results.
    Następnie w pętli while wprowadzamy warunki zgodne z poleceniem --> jeśli suma kwadratów cyfr aktualnej liczby z procesu będzie 1 lub pojawi się kolejny raz to zatrzymujemy pętlę
    W else mamy po prosu warunek: przeprowadzamy kolejne operacje dodawania kwadratów cyfr i dodajemy je do listy results
    Na samym końcu sprawdzamy czy 1 występuje w liście z wynikami procesów to znaczy, że ta liczba JEST WESOŁA, w przeciwnym wypadku zwracamy False
    """
    current = squared(num)
    results = [current]

    while True:
        if current == 1 or get_count(results, current) > 1:
            break
        else:
            current = squared(current)
            results.append(current)

    if 1 in results:
        return True, len(results)
    return False
# tworzymy słownik, który będzie przechowywał liczbę od 1 do 1000 (klucz) oraz ilość liczb wesołych otrzymanych w cyklu obliczeniowym
how_many_happy = {}
for i in range(1, 1001):
    if is_happy(i):
        how_many_happy.update({i: is_happy(i)[1]})

maxNumOfHappy = get_max(get_values_dict(how_many_happy)) # wyznaczamy maxa

print(maxNumOfHappy)
output = []
for num in how_many_happy:
    if how_many_happy[num] == maxNumOfHappy: # wypisujemy wyjściowe liczby o maksymalnej ilości liczb wesołych w cyklu obliczeniowym
        print(num, end=" ")
        output.append(num)

with open("wyniki4.txt", "w", encoding="UTF-8") as out:
    out.write("ZADANIE 4.1:\n")
    out.write(f"{maxNumOfHappy}\n")
    for happy in output:
        out.write(f"{happy} ")
    out.write("\n")