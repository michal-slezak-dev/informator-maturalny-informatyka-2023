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

for number in numbers:
    for i in range(3, number, 2):
        if is_even(number):
            if is_prime(i) and is_prime(number - i):
                print(number, " ", i, " ", number - i)
                break