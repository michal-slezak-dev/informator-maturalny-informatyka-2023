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

def if_palindromic(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

with open("danePracaDomowa1.txt", "r", encoding="UTF-8") as file:
    numbers = []

    for line in file:
        numbers.append(line.strip())
# print(numbers)

counter = 0

answers = []
print("Te liczby to:")
for number in numbers:
    """Pierwszy sposób"""
    # if if_palindromic(number) or if_palindromic(int(number, 16)):
    #     counter += 1
    #     print(number, " ", int(number, 16))

    """Drugi sposób"""
    if if_palindromic(number) or if_palindromic(from_other(number, 16)):
        counter += 1
        print(number, " ", from_other(number, 16))
        answers.append([number, from_other(number, 16)])

print(f'\nTych liczb jest: {counter}')

with open("zadanie1.txt", "w", encoding="UTF-8") as output:
    for answer in answers:
        for num in answer:
            output.write(str(num) + " ")
        output.write("\n")
    
    output.write(str(counter))