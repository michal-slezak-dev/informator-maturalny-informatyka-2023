def is_smaller(pair1, pair2):
    """
    Tutaj dosłownie przepisuję warunek z polecenia ;-)
    :param pair1:
    :param pair2:
    :return:
    """
    actualNum1 = int(pair1[0])
    actualNum2 = int(pair2[0])

    actualWord1 = pair1[1]
    actualWord2 = pair2[1]

    if -1 * actualNum1 < actualNum2 or -1 * actualNum1 == actualNum2 and actualWord1 < actualWord2:
        return True
    return False


with open("pary.txt", "r") as file:
    pairs = []

    for line in file:
        pairs.append(line.split())

pairs_num_equal_to_len = []

# Tutaj do listy pairs_num_equal_to_len dodaję te pary, gdzie liczba jest równa długości danego słowa
for pair in pairs:
    if int(pair[0]) == len(pair[1]):
        pairs_num_equal_to_len.append(pair)

"""
Tutaj tworzę dwie pętle, w pierwszej zaczynamy od 0 a w drugiej od 1 - potrzebne jest to , żeby porównywać każdą parę z każdą inną.
Na koniec, przypisuję zmiennej theSmallest parę, która jest mniejsza od wszystkich innych.


"""
for i in range(len(pairs_num_equal_to_len)):
    for j in range(1, len(pairs_num_equal_to_len)):
        if is_smaller(pairs_num_equal_to_len[i], pairs_num_equal_to_len[j]):
            theSmallest = pairs_num_equal_to_len[i]

print(f'{theSmallest[0]} {theSmallest[1]}')

with open("wyniki4.txt", "a", encoding="UTF-8") as output:
    output.write("\n\nZADANIE 4.3\n")
    output.write(theSmallest[0] + " " + theSmallest[1])