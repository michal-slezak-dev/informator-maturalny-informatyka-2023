def to_other(number, base):
    result = []
    newNum = ""

    letters = ["A", 10, "B", 11, "C", 12, "D", 13, "E", 14, "F", 15]

    more_than_10 = dict()
    for i in range(0, 11, 2):
        more_than_10.update({letters[i + 1]: letters[i]})

    while number > 0:
        temp = number % base
        result.append(str(temp))
        number //= base

    for char in result:
        if int(char) in list(more_than_10.keys()):
            result[result.index(char)] = more_than_10[int(char)]

    return newNum.join(result[::-1])    

def if_antipalindromic(number):
    number = str(number)
    for i in range(1, int(len(number) / 2) + 1):
        if number[i - 1] == number[len(number) - i]:
            return False
    return True

with open("danePracaDomowa2.txt", "r", encoding="UTF-8") as file:
    numbers = []

    for line in file:
        numbers.append(line.strip())
# print(numbers)

counter = 0
answers = []
print("Te liczby to:")
for number in numbers:
    if if_antipalindromic(number) and if_antipalindromic(to_other(int(number), 14)):
        print(number, " ", to_other(int(number), 14))
        counter += 1
        answers.append([number, to_other(int(number), 14)])

print(f'Tych liczb jest: {counter}')

with open("zadanie2.txt", "w", encoding="UTF-8") as output:
    for answer in answers:
        for num in answer:
            output.write(str(num) + " ")
        output.write("\n")
    output.write(str(counter))