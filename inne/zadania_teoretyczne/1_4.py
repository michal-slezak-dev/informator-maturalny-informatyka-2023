n = int(input())
T = [input() for _ in range(n)]

""" 
Zmienna b będzie przechowywać nasz wynik(rozmiar skompresowanego tekstu T),
Zmienna skom będzie przechowywać skompresowany tekst T, licz będzie przechowywaćliczbę wystąpień po sobie danego znaku,
znak będzię przechowywać znak, który się powtarza po kolei.

jak mamy ***##!!* ---> porównujemy:
* z *
* z *
* z #
# z #
# z !
! z !
! z *
"""
b = 0
skom = ''
licz = 1
znak = T[0]

for i in range(1, n):
    if T[i - 1] == T[i]: # Jeśli taki sam znak to zwiększamy licz i znak = T[i - 1](obecnemu)
        licz += 1
        znak = T[i - 1]
    else:                           
        skom += f"{licz}{znak}"  # Jeśli nie to dopisujemy aktualna ilosc znaku danego do skom i potem licz = 1, znak = T[i](kolejny znak, który nie jest taki sam)
        licz = 1
        znak = T[i]

skom += f"{licz}{znak}" # dodajemy ostanią wartość dla zmiennej licz i znak, dla ***##!!* --> 1*(bo ostatni znak występuje raz)

b = len(skom)
print(b)
# print(skom)
