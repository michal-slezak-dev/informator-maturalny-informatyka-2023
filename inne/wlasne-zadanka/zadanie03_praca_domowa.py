def fixed_numbers(numberStr):
    fixedNum = ""

    for char in numberStr:
        if char.isdigit():
            fixedNum += char

    return fixedNum

def from_other(number, base):
    result = []
    convertedNum = ""

    number = str(number)
    reversedNum = list(number[::-1].upper())

    letters = ["A", "10", "B", "11", "C", "12", "D", "13", "E", "14", "F", "15"]

    more_than_10 = dict()
    for i in range(0, 11, 2):
        more_than_10.update({letters[i]: letters[i + 1]})

    for char in reversedNum:
        if char in list(more_than_10.keys()):
            reversedNum[reversedNum.index(char)] = more_than_10[char]
            
    for i in range(len(number)):
        result.append(int(reversedNum[i]) * (base ** i))

    return convertedNum.join(str(sum(result)))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

with open("danePracaDomowa3.txt", "r", encoding="UTF-8") as file:
    numbers = []

    for line in file:
        numbers.append(line.strip())
# print(numbers)

for number in numbers:
    numbers[numbers.index(number)] = fixed_numbers(number)

# Tworzymy zmienną counter, która będzie zliczać wiersze z tymi liczbami
# Tworzymy też listę answers, która będzie przechowywać odpowiedzi do zadania, przyda nam się przy zapisywaniu do pliku
counter = 0
answers = []

# Pętla ta przechodzi przez listę z danymi z pliku
# Sprawdzamy czy po zamianie z liczby piątkowej na dziesiętną mamy do czynienia z liczbą pierwszą
# Jeśli jest to liczba pierwsza to wypisujemy ją w systemie oktalnym, dodajemy taką liczbę w systemie oktalnym do listy answers i zwiększamy licznik o 1

print(f'Te liczby to:')
for number in numbers:
    """Można też zamiast funkcji from_other użyć po prostu int(liczba, podstawa), to też zamieni nam liczbę w danym systemie na liczbę dziesiętną"""
    if is_prime(int(from_other(number, 5))):
        print(str(oct(int(number))).lstrip("0o"))
        answers.append(str(oct(int(number))).lstrip("0o"))
        counter += 1
print(f'Tych liczb jest {counter}')

with open("zadanie3.txt", "w", encoding="UTF-8") as output:
    for num in answers:
        output.write(str(num) + "\n")
    output.write(str(counter))