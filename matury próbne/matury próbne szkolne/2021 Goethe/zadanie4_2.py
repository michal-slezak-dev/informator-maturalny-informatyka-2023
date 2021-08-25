def people_nobody_knows(people_who_know_others_list, n):
    #Ta lista przechowuje numery osób od 0 do n - 1
    people = []

    for i in range(n):
        people.append(str(i))
    # print(people)

    # w tej liście mamy numery osób, które zna dana osoba
    friendsNumber = {}

    # Tutaj mamy numery osób, które zna dana osoba
    for i in range(n):
        friendsNumber.update({i: people_who_know_others_list[i][1:]})
    # print(friendsNumber)

    # Do tej listy dodajemy nuumery osób, które są znane przez jakieś inne osoby
    peopleNumbers = []

    for personNumber in friendsNumber:
        peopleNumbers.append(friendsNumber[personNumber])
    # print(peopleNumbers)

    # lista, która ma będzie przechowywała numery osób, które znają dane osoby
    friendsNumbersAll = []

    # dodajemy do listy friendsNumbersAll numery osób, które zna dana osoba
    for friend in peopleNumbers:
        for numbers in friend:
            friendsNumbersAll.append(numbers)
    # print(friendsNumbersAll)

    personNobodyKnows = []

    # print(people)

    # sprawdzamy czy numer danej osoby jest w liście, która przechowuje numery osób, które są znane przez inne osoby, jeśli nie ma
    # to numer osoby,której nikt nie zna jest dodawany do listy personNobodyKnows,
    for i in range(n):
        if people[i] not in friendsNumbersAll:
            personNobodyKnows.append(people[i])
    # print(personNobodyKnows)

    # jeżeli lista przechowująca numer/numery osób, których nikt nie zna jest pusta, to znaczy, że nie ma takiej osoby i zwracamy -1
    # w przeciwnym przypadku wypisujemy numer tej osoby

    numbersNobodyKnows = []

    if not personNobodyKnows:
        return -1
    else:
        for personNumberNobodyKnows in personNobodyKnows:
            numbersNobodyKnows.append(personNumberNobodyKnows)
    return numbersNobodyKnows

with open("znajomi_1.txt", "r", encoding="UTF-8") as file_1:

    n1 = int(file_1.readline())       #liczba osób
    people_who_know_others_1 = []

    for line in file_1:
        people_who_know_others_1.append((line.strip("\n")).split())
# print(f'\nOsoby, których nikt nie zna mają numery: {people_nobody_knows(people_who_know_others_1, n1)}')

with open("znajomi_2.txt", "r", encoding="UTF-8") as file_2:

    n2 = int(file_2.readline())       #liczba osób
    people_who_know_others_2 = []

    for line in file_2:
        people_who_know_others_2.append((line.strip("\n")).split()) #dodajemy kolejne linijki
# print(f'\nOsoby, których nikt nie zna mają numery: {people_nobody_knows(people_who_know_others_2, n2)}')

###ODPOWIEDZI###
print("Osoby z pliku znajomi_1.txt, których nikt nie zna mają numer/-y: ")
for number in people_nobody_knows(people_who_know_others_1, n1):
    print(number, end=" ")

print("\nOsoby z pliku znajomi_2.txt, których nikt nie zna mają numer/-y: ")
for number in people_nobody_knows(people_who_know_others_2, n2):
    print(number, end=" ")


with open("wyniki_zadanie4_2.txt", "w", encoding="UTF-8") as output_file:
    output_file.write("Zadanie 4.2\n")
    output_file.write("Osoby z pliku znajomi_1.txt, których nikt nie zna mają numer/-y: ")
    for number in people_nobody_knows(people_who_know_others_1, n1):
        output_file.write(number)

with open("wyniki_zadanie4_2.txt", "a", encoding="UTF-8") as output_file:
    output_file.write("\nOsoby z pliku znajomi_2.txt, których nikt nie zna mają numer/-y: ")
    for number in people_nobody_knows(people_who_know_others_2, n2):
        output_file.write(number)
        output_file.write(", ")
