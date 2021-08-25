def pairs(people_who_know_others_list, n):
    # Ta lista przechowuje numery osób od 0 do n - 1
    people = []

    for i in range(n):
        people.append(str(i))

    # w tej liście mamy numery osób, które zna dana osoba
    friendsNumber = {}

    # Tutaj mamy numery osób, które zna dana osoba
    for i in range(n):
        friendsNumber.update({i: people_who_know_others_list[i][1:]})

    pairs_friends = []
    for personNumber in friendsNumber:
       pairs_friends.append(friendsNumber[personNumber])
    return pairs_friends #zwracamy listę np dla pliku znajomi_1.txt [['2', '3', '4'], ['2'], ['3', '1', '4'], ['4', '1'], ['1']]

def display_pairs(pairs_func):
    friendNumber = 0

    #ta lista będzie przechowywać pary osób
    pairs_friends = []

    #w tej pętli tworzymy pary i zwiększamy za każdym obrotem 1. pętli friendNumber, który reprezentuje numer osoby od 0 do n - 1
    #do listy pairs_friends dodajemy utworzone pary, rozdzielamy pair splitem po spacji
    for personNumber in pairs_func:
        for i in range(len(personNumber)):
            pair = str(friendNumber) + " " + str(personNumber[i])
            pairs_friends.append(pair.split(" "))
        friendNumber += 1

    #sortujemy pary np. [['1', '2'], ['2', '1']] -->  [['1', '2'], ['1', '2']]
    for pair in pairs_friends:
        pair = pair.sort()

    #tworzymy zbiór, który będzie przechowywał nasze odpowiedzi(pary), które znają siebie wzajemnie
    answers_set = set()

    #dla każdej pary w liście pairs_friends sprawdzamy czy występuje więcej niż 1 raz, jeśli tak to oznacza to, że te osoby znają się wzajemnie
    # ['1', '2'] to samo co posortowana para ['2', '1']
    # jeśli spełniony jest warunek to do zbioru dodajemy naszą parę, nie jako listę, ale jako tuple
    for pair in pairs_friends:
        if pairs_friends.count(pair) > 1:
            answers_set.add(tuple(pair))
    return list(answers_set) #na koniec zwracamy nasz zbiór, który nie ma duplikatów par


###ODPOWIEDZI###

#ZNAJOMI_1.TXT
with open("znajomi_1.txt", "r", encoding="UTF-8") as file_1:

    n1 = int(file_1.readline())       #liczba osób
    people_who_know_others_1 = []

    for line in file_1:
        people_who_know_others_1.append((line.strip("\n")).split())
# print(n1)
# print(people_who_know_others_1)

#ZNAJOMI_2.TXT
with open("znajomi_2.txt", "r", encoding="UTF-8") as file_2:

    n2 = int(file_2.readline())       #liczba osób
    people_who_know_others_2 = []

    for line in file_2:
        people_who_know_others_2.append((line.strip("\n")).split())
# print(n2)
# print(people_who_know_others_2)

#ZNAJOMI_1.TXT
#dla każdej pary w zwróconym zbiorze bierzemy numer osoby z tej pary i wypisujemy
print("Pary numerów, które znają się nawzajem dla pliku znajomi_1.txt: ")
for pair1 in display_pairs(pairs(people_who_know_others_1, n1)):
    for number1 in pair1:
        print(number1, end=" ")
    print()
print()

#ZNAJOMI_2.TXT
#dla każdej pary w zwróconym zbiorze bierzemy numer osoby z tej pary i wypisujemy
print("Pary numerów, które znają się nawzajem dla pliku znajomi_2.txt: ")
for pair2 in display_pairs(pairs(people_who_know_others_2, n2)):
    for number2 in pair2:
        print(number2, end=" ")
    print()


with open("wyniki_zadanie4_3.txt", "w", encoding="UTF-8") as outputfile:
    outputfile.write("Zadanie 4_3\n")
    outputfile.write("Pary numerów, które znają się nawzajem dla pliku znajomi_1.txt: \n")
    for pair1 in display_pairs(pairs(people_who_know_others_1, n1)):
        for number1 in pair1:
            outputfile.write(str(number1) + " ")
        outputfile.write("\n")

with open("wyniki_zadanie4_3.txt", "a", encoding="UTF-8") as outputfile:
    outputfile.write("\nPary numerów, które znają się nawzajem dla pliku znajomi_2.txt: \n")
    for pair2 in display_pairs(pairs(people_who_know_others_2, n2)):
        for number2 in pair2:
            outputfile.write(str(number2) + " ")
        outputfile.write("\n")
