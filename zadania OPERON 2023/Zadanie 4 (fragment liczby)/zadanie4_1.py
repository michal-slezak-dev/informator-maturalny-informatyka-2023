with open("dane_liczbowe.txt", "r") as file:
    nums = [(line.strip().split()[0], int(line.strip().split()[1])) for line in file]

# counter --> zlicza ilość licz, które na k-pozycji mają cyfrę podzielną przez 2
# sum zlicza sumę cyfr liczb na k-pozycji
counter = 0
sum = 0
for pair in nums:
    if int(pair[0][pair[1] - 1]) % 2 == 0:
        counter += 1
    sum += int(pair[0][pair[1] - 1])

print(counter)
print(sum)

with open("wynik4.txt", "w") as out:
    out.write("4.1:\n")
    out.write(f"{counter}\n{sum}\n\n")
