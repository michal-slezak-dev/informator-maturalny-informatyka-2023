with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

counter = 0  # zlicza ilość par takich, że a + b = c
nums_ans = []  # zawiera tuple z trojkami liczb a, b, c --> takie że a + b = c oraz długość a < długość b < długość c
for i in range(2, len(nums)):
    if nums[i - 2] + nums[i - 1] == nums[i]:
        counter += 1
        if len(str(nums[i - 2])) < len(str(nums[i - 1])) < len(str(nums[i])):
            nums_ans.append((nums[i - 2], nums[i - 1], nums[i]))

print(f"a) {counter}\nb)")

with open("wyniki3.txt", "a") as out:
    out.write("3.2\n")
    out.write(f"a) {counter}\nb)\n")
    for abc in nums_ans:
        print(f"{abc[0]} {abc[1]} {abc[2]}")
        out.write(f"{abc[0]} {abc[1]} {abc[2]}\n")