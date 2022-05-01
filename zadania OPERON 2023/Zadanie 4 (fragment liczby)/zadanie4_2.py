from collections import deque
from copy import deepcopy

def is_palindromic(num):
    return num == num[::-1]

with open("dane_liczbowe.txt", "r") as file:
    nums = [[list(line.strip().split()[0]), line.strip().split()[1]] for line in file]

"""
1. robimy deep kopię naszej listy (liczby n) i dodajemy na poczatek k,
2. sprawdzamy czy jest to palindrom (po zamianie na string),
3. dodajemy do listy z odpowiedziami zamienioną na inta liczbę pierwotną (n)
4. sortujemy listę z liczbami, które spełniają warunki zadania
5. wypisujemy odpowiedzi
"""
nums_answ = []
for pair in nums:
    num_c = deque(deepcopy(pair[0]))
    num_c.appendleft(pair[1])

    if is_palindromic(''.join(list(num_c))):
        nums_answ.append(int(''.join(pair[0])))

nums_answ = sorted(nums_answ)
with open("wynik4.txt", "a") as out:
    out.write("4.2:\n")
    for num in nums_answ:
        print(num)
        out.write(f"{num}\n")
