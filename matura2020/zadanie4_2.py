def sub_seq(word):
    """
    Na początku tworzę 2 zmienne - letter i counter, letter będzie przechowywać literkę, która wstępuje najwięcej razy po sobie, counter będzie przechowywać ilość wystąpień tej literki po sobie.
    Następnie, tworzę 2 listy - counters i letters, w których będę przechowywać aktualne ilości występowania literek po sobie i same literki, które daną ilośc razy wystąpiły.

    Przechodzimy do pętli, która zaczyna się od 1, żeby nie wyjść poza zakres listy z danymi. Na początku sprawdzam czy następna literka w słowie jest taka sama jak poprzednia,
    jeśli tak to zwiększam counter o 1 i zmiennej letter przypisuję aktualną literkę.

    W przeciwnym wypadku counter ustawiamy na 1 i letter na pierwszy znak tego słowa, gdyż są takie słowa, w którch każda litera występuje po sobie tylko raz.
    Następnie, sprawdzam czu letter nie jest puste, jeśli nie to wtedy do list coutners i letters dodaję zmienne counter i letter,
    w przeciwnym wypadku dodaję 1 i pierwszą literkę danego słowa, gdyż oznacza to, że każda literka występuje po sobie tylko raz, np.
    słowo: 'abcdefgh' lub słowo: 'a'

    Na końcu używam     bloku try except. Staram się wyłonić maksa z counters i wtedy przypisuję do zmiennej maxSubLetter literkę, która wystąpiła tyle razy.
    Kiedy wypluwa mi ValueError to znaczy, że coś się popsuło i mamy pustą listę counters i oznacza to, że to ten przypadek, gdzie każda literka występuje po sobie tylko raz i
    trzeba maxSub przypisac 1 i ta literka to pierwsza literka prawdzanego słowa. Na koniec zwracamy 'wiadomość' składającą się z tej literki * ilość jej występowania po sobie.

    :param word:
    :return:
    """
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
    output.write("\n\nZADANIE 4.2 \n")
    for word in words:
        output.write(sub_seq(word) + "\n")