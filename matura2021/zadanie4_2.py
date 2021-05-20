with open("instrukcje.txt", "r") as file:
    instructions = []

    for line in file:
        instructions.append(line.split())

only_instructions = []

for instruction in instructions:
    only_instructions.append(instruction[0])

amount_and_instruction = []

for i in range(1, len(only_instructions)):
    if only_instructions[i] == only_instructions[i - 1]:
        counter += 1
    else:
        counter = 1
    amount_and_instruction.append([only_instructions[i], counter])

only_amount = []

for instruction in amount_and_instruction:
    only_amount.append(instruction[1])

maxAmount = max(only_amount)

for instruction in amount_and_instruction:
    if instruction[1] == maxAmount:
        maxInstruction = instruction[0]

print(maxInstruction, " ", maxAmount)



