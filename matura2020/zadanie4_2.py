def sub_seq(word):
    counter = 1
    letters = []
    counters = []

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            counter += 1
            letter = word[i]
        else:
            counter = 1
            letter = ""
        if letter != '':
            letters.append(letter)
            counters.append(counter)
        else:
            letters.append(word[0])
            counters.append(1)
    try:
        maxSub = max(counters)
        maxLetterSub = letters[counters.index(maxSub)]

        return (maxLetterSub * maxSub) + " " + str(maxSub)
    except ValueError:
        maxSub = 1
        maxLetterSub = word[0]

        return (maxLetterSub * maxSub) + " " + str(maxSub)



with open("pary.txt", "r") as file:
    words = []

    for line in file:
        words.append(line.split()[1].strip())

# print(sub_seq(words[37]))

for word in words:
    print(sub_seq(word))