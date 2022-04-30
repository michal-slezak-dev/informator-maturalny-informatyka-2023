from math import gcd

with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

counter = 0  # będzie zliczać ilość liczb względnie pierwszych
for i in range(1, len(nums)):
    if gcd(nums[i - 1], nums[i]) == 1:
        counter += 1

print(counter)

with open("wyniki3.txt", "w") as out:
    out.write("3.1:\n")
    out.write(f"{counter}\n\n")