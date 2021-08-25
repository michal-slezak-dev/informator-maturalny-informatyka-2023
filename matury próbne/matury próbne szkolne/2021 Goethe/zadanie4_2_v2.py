def people_nobody_knows(people_who_know_others_list, n):
    people = []

    #do listy people zapisujemy numery osób od 0 do n - 1
    for i in range(n):
        people.append(str(i))

    #do listy person_somebody_knows zapisujemy numery osób, które dana osoba zna
    person_somebody_knows = []
    for personNumber in people_who_know_others_list:
        person_somebody_knows.append(personNumber[1:]) # od [1:], bo pod indeksem 0 jest info o tym ile osób zna ta osoba

    #sprawdzamy, jeśli osoba, którą dana osoba zna jest w liście people to wykreślamy ją
    #jeśli zostanie jakaś liczba w liście people to ta liczba będzie numerem osoby, której nikt nie zna
    for friendPersonKnows in person_somebody_knows:
        for i in range(len(friendPersonKnows)):
            if friendPersonKnows[i] in people:
                people.remove(friendPersonKnows[i])

    if not people:
        return -1
    return people

with open("znajomi_1.txt", "r", encoding="UTF-8") as file_1:
    n1 = int(file_1.readline())
    people_who_know_others1 = []

    for line in file_1:
        people_who_know_others1.append((line.strip("\n")).split())
# print(people_who_know_others1)

with open("znajomi_2.txt", "r", encoding="UTF-8") as file_12:
    n2 = int(file_12.readline())
    people_who_know_others2 = []

    for line in file_12:
        people_who_know_others2.append((line.strip("\n")).split())
# print(people_who_know_others2)

#PLIK ZNAJOMI_1.TXT
print("W pliku znajomi_1.txt, osoba/-y, której/-ych nikt nie zna to osoby o numerze/-ach: ")
for personNumber in people_nobody_knows(people_who_know_others1, n1):
    print(personNumber, end=" ")
print()

#PLIK ZNAJOMI_2.TXT
print("W pliku znajomi_2.txt, osoba/-y, której/-ych nikt nie zna to osoby o numerze/-ach: ")
for personNumber in people_nobody_knows(people_who_know_others2, n2):
    print(personNumber, end=" ")
