def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return  None


lista = [1, 3, 5, 6, 8, 12]
print(binary_search(lista, 12))