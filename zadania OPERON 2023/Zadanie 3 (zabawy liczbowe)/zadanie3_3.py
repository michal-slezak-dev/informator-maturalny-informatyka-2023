def is_prime(num):
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

counter = 1
""" 
Zlicza długość danego podciągu rosnącego liczb pierwszych
(zaczynamy od 1, bo najkrótszy będzie się składał z 1 liczby)
"""
max_sub = []  # zawiera długości danych podciągów
for i in range(1, len(nums)):
    if is_prime(nums[i - 1]) and is_prime(nums[i]) and nums[i] > nums[i - 1]:
        counter += 1
    else:
        counter = 1
    max_sub.append(counter)

"""
first_num i last_num odpowiednio zawierają pierwszą i ostatnią liczbę najdłuższego ciągu,
indeks pierwszego elementu to indeks max countera z listy max_sub + 2 - longest_sub, bo 
wtedy wyjdzie nam poprawny indeks (inaczej nie będziemy mogli odjąć maksymalnej długości):

weźmy tablicę [5, 7, 11] --> max_sub = [2, 3]

indeks max countera to 1, aby otrzymać pierwszą liczbę trzeba dodać 2 -> 2 + 1 = 3 oraz odjąć max counter, czyli
3 - 3 = 0 --> jest to indeks 1. elementu ciągu (w tablicy nums)

indeks ostatniego elementu to indeks max countera z max_sub + 1, bo inaczej nie otrzymamy poprawnego indeksu i nie 
będziemy mogli odjąć max countera:

weźmy tablicę [5, 7, 11] --> max_sub = [2, 3]

indeks max countera to 1, aby otrzymać ostatnią liczbę trzeba dodać 1 -> 1 + 1 = 2,czyli
indeks ostatniej liczby to 2 (w tablicy nums)
"""
longest_sub = max(max_sub)  # wyłaniamy długość najdłuższego podciągu
first_num, last_num = nums[max_sub.index(longest_sub) + 2 - longest_sub], nums[max_sub.index(longest_sub) + 1]
print(f"a) {longest_sub}\nb) Pierwsza liczba: {first_num}\nOstatnia liczba: {last_num}")

with open("wyniki3.txt", "a") as out:
    out.write("\n3.3\n")
    out.write(f"a) {longest_sub}\nb) Pierwsza liczba: {first_num}\nOstatnia liczba: {last_num}")