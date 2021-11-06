def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def czy_reszta_to_1(n):
    if n % 4 == 1:
        return True
    return False

def znajdz_sume_kwadratow(n):
    for i in range(1, n):
        for k in range(i + 1, n):
            if i * i + k * k == n: #if i**2 + k**2 == n:
                return f"{i}^2 + {k}^2"

n = int(input())

if czy_pierwsza(n) and czy_reszta_to_1(n):
    print(znajdz_sume_kwadratow(n))           