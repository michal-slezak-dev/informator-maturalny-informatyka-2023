def sub_seq(word):
    letter = ""
    counter = 1
    counters = []
    letters = []

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            counter += 1
            letter = word[i]
        else:
            counter = 1
            letter = word[0]

        if letter != '':
            counters.append(counter)
            letters.append(letter)
        else:
            counters.append(1)
            letters.append(word[0])

    try:
        maxSub = max(counters)
        maxSubLetter = letters[counters.index(maxSub)]
    except ValueError:
        maxSub = 1
        maxSubLetter = word[0]
    finally:
        return f'{maxSub * maxSubLetter}  {maxSub}'


with open("pary.txt", "r") as file:
    words = []

    for line in file:
        words.append(line.split()[1])

for word in words:
    print(sub_seq(word))

with open("wyniki4.txt", "a", encoding="UTF-8") as output:
    output.write("\n\n ZADANIE 4.2 \n\n")
    for word in words:
        output.write(sub_seq(word) + "\n")
