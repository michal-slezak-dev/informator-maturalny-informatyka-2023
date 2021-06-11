def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

with open("pary.txt", "r") as file:
    numbers = []

    for line in file:
        numbers.append(int(line.split()[0]))

# To jest potrzebne do zapisania do pliku
out = []
"""
Tutaj najpierw sprawdzam czy liczba z pliku jest parzysta - jeśli tak to przechodzę dalej.
Potem robię pętlę, która się zaczyna od 3 i skok to 2, bo szukam liczb nieparzystych(pomijam parzyste), i zakładam, że każde i jest pierwszą liczbą,
następnie sprawdzam czy to i jest rzeczywiście liczbą pierwszą i czy różnica liczba - i też jest liczbą pierwszą - jeśli tak to jest to nasza suma i 
robimy breaka, bo nie ma sensu już dalej szukać.
"""
for number in numbers:
    if is_even(number):
        for i in range(3, number, 2):
            if is_prime(i) and is_prime(number - i):
                print(number, " ", i, " ", number - i)
                out.append(str(number) + " " + str(i) + " " + str(number - i))
                break

# zapis do pliku
with open("wyniki4.txt", "w", encoding="UTF-8") as output:
    output.write("ZADANIE 4.1\n")
    for outp in out:
        output.write(str(outp) + "\n")