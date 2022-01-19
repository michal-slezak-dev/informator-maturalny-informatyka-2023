def pow(num, base):
    res = 1

    while base > 0:
        res *= num
        base -= 1

    return res

def search(list, target):
    if target not in list:
        return None

    for i in range(len(list)):
        if list[i] == target:
            return i

def get_count(list, target):
    counter = 0

    for element in list:
        if element == target:
            counter += 1

    return counter

def get_max(list):
    max_current = -12312

    for element in list:
        if element > max_current:
            max_current = element

    return max_current

def squared(num):  # 7 --> 49 | 49 --> 4^2 + 9^2 ->97
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
        return True
    return False

with open("liczby (1).txt", "r") as file:
    nums = []
    for line in file:
        nums.append(int(line.strip()))

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
maxSub = get_max(subsequence) # wyłaniamy długość najdłuższego podciągu liczb wesołych
# indexOfMaxSub = search(subsequence, maxSub) # wyłaniamy index tej maksymalenj długości
indexOfMaxSub = subsequence.index(maxSub) # tak też można, lepszy sposób, ponieważ przeszukiwanie liniowe może się wysypać na większych listach
lastHappy = nums_seq[indexOfMaxSub] # ostatnia liczba szczęśliwa najdłuższego podciągu ma taki sam index jak ta największa wartość (maxSub)
firstHappy = nums_seq[indexOfMaxSub - maxSub + 1] # pierwsza liczba szczęśliwa najdłuższego podciągu ma index maksymalnej długości - ta długość + 1, bo indeksujemy od zera

print(f"{maxSub} {firstHappy} {lastHappy}")

with open("wyniki4.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 4.3:\n")
    out.write(f"{maxSub} {firstHappy} {lastHappy}\n\n")