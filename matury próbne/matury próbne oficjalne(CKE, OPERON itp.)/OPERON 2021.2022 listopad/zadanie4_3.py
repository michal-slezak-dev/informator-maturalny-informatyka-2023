def squared(num):  # 7 --> 49 | 49 --> 4^2 + 9^2 ->97
    res = 0
    for digit in str(num):
        res += int(digit) ** 2

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
        if current == 1 or results.count(current) > 1:
            break
        else:
            current = squared(current)
            results.append(current)

    if 1 in results:
        return True
    return False

with open("liczby (1).txt", "r") as file:
    nums = [int(line.strip()) for line in file]

subsequence = [] # ta lista będzie przechowywać dlugość aktualnego podciągu
nums_seq = [] # ta lista będzie przechowywać liczbę wesołą, która jest elementem danego podciągu
counter = 0
for i in range(1, len(nums)):
    if is_happy(nums[i - 1]):
        counter += 1
        subsequence.append(counter)
        nums_seq.append(nums[i - 1])
    else:
        counter = 0
maxSub = max(subsequence) # wyłaniamy długość najdłuższego podciągu liczb wesołych
indexOfMaxSub = subsequence.index(maxSub) # wyłaniamy index tej maksymalenj długości
lastHappy = nums_seq[indexOfMaxSub] # ostatnia liczba szczęśliwa najdłuższego podciągu ma taki sam index jak ta największa wartość (maxSub)
firstHappy = nums_seq[indexOfMaxSub - maxSub + 1] # pierwsza liczba szczęśliwa najdłuższego podciągu ma index maksymalnej długości - ta długość + 1, bo indeksujemy od zera

print(f"{maxSub} {firstHappy} {lastHappy}")

with open("wyniki4.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 4.3:\n")
    out.write(f"{maxSub} {firstHappy} {lastHappy}\n\n")