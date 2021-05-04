import random
import string

def broken_string(s):
    """Ta funkcja "psuje" napis poprzez dodawanie do niej losowych i losowo znaków specjalnych"""
    punctuation = list(string.punctuation)
    s = list(s)

    brokenStr = ""

    for i in range(random.randint(1, 5)):
        randomPunc = random.choice(punctuation)
        s.insert(random.randint(0, len(s)), randomPunc)

    return brokenStr.join(s)

def fixed_numbers(numberStr):
    fixedNum = ""

    for char in numberStr:
        if char.isdigit():
            fixedNum += char

    return fixedNum


def to_other(number, base):
    """Ta funkcja zamienia liczbę dziesiętną na dany system."""
    # Lista result będzie przechowywać zamienioną liczbę a newNum taką liczbę jako string
    result = []
    newNum = ""

    letters = ["A", 10, "B", 11, "C", 12, "D", 13, "E", 14, "F", 15]
    # Tworzymy słownik, którry przechowuje w kluczach liczby od 10 do 15 a w wartościach literki od A do F
    more_than_10 = dict()
    for i in range(0, 11, 2):
        more_than_10.update({letters[i + 1]: letters[i]})

    # Dopóki liczba jest większa od 0 to do zmiennej temp przypisujemy resztę z dzielenia tej liczby przez podstawę danego systemu
    # Do listy result dodajemy temp(reszta z dzielenia)
    # Na koniec dzielimy liczbę całkowicie przez daną podstawę
    # Dokładne wyjaśnienia jak to działa są na tym obrazku: https://www.tutorialspoint.com/basics_of_computers/images/decimal_to_binary.jpg
    # https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm
    while number > 0:
        temp = number % base
        result.append(str(temp))
        number //= base

    # Jeżeli chcemy zamienić liczbę na system o podstawie 10-16 to potrzebujemy literek od A(10) - F(15)
    # W tej pętli po prostu sprawdzamy czy w reszta z dzielenia tej liczby przez podstawędanego systemu jest w  kluczach słownika
    # To wtedy zamieniamy taką resztę na odpowiadającą jej literkę
    for char in result:
        if int(char) in list(more_than_10.keys()):
            result[result.index(char)] = more_than_10[int(char)]
    # Na koniec zwracami odwróconą listę result jako string dodany do pustego stringa newNum()
    return newNum.join(result[::-1])    

def from_other(number, base):
    """Ta funkcja przelicza liczbe z danego systemu na dziesietny"""
    # Lista result będzie przechowywać zamienioną liczbę a convertedNum taką liczbę jako string
    result = []
    convertedNum = ""

    #Zamieniamy liczbę w innym systemie na stringa i w zmiennej reversedNum przechowujemy odwróconą liczbę
    number = str(number)
    reversedNum = list(number[::-1].upper())

    letters = ["A", "10", "B", "11", "C", "12", "D", "13", "E", "14", "F", "15"]
    # Tworzymy słownik, którry przechowuje w kluczach literki a w wartościach liczby od 10 do 15
    more_than_10 = dict()
    for i in range(0, 11, 2):
        more_than_10.update({letters[i]: letters[i + 1]})

    # Dla każdego znaku w odwróconej liczbie do konwersji sprawdzamy czy jest w kluczach
    # Jeśli tak to zamieniamy ten znak na liczbę
    for char in reversedNum:
        if char in list(more_than_10.keys()):
            reversedNum[reversedNum.index(char)] = more_than_10[char]
    
    # W tej pętli dokonuje się konwersja liczby z danego systemu na system dziesiętny
    # Do listy result dodajemy liczbę z ze stringa reversedNum i mnożymy ją przez podstawę tego systemu, z którego zamieniamy
    # Pętla się obraca tyle razy, ile jest elementów w stringu/listy result, gdyż:
    # np. mamy liczbę w systemie dwójkowym 10010010 to robimy tak: 0 * 2^0 + 1 * 2^1 + 0 * 2^2 itd.
    for i in range(len(number)):
        result.append(int(reversedNum[i]) * (base ** i))
    # Na koniec zwracamy jako string sumę liczb w liście result
    return convertedNum.join(str(sum(result)))
"""Testy"""
# print(to_other(107012833242, 13))
# print(from_other("18ea763fda", 16))
# print(fixed_numbers("1.4%12.4&51"))

"""GENEROWANIE DANYCH DO ZADANIA01"""
# with open("danePracaDomowa1.txt", "w") as dataFile:
#     for i in range(1000):
#         randomNum = random.randint(25000, 2000000)
#         dataFile.write(str(to_other(randomNum, 16)) + "\n")

"""GENEROWANIE DANYCH DO ZADANIA02"""
# with open("danePracaDomowa2.txt", "w") as dataFile:
#     for i in range(1000):
#         randomNum = random.randint(50000, 3500000)
#         dataFile.write(str(randomNum) + "\n")

#TO DO:
"""GENEROWANIE DANYCH DO ZADANIA03"""
# with open("danePracaDomowa3.txt", "w") as dataFile:
#     for i in range(1000):
#         randomNum = random.randint(100000, 5500000)
#         dataFile.write(str(broken_string(to_other(randomNum, 5))) + "\n")