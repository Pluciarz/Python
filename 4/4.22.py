def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

def liczba_silna(n):
    suma = 0
    kopia = n
    max = 1
    kmax = 1
    while max <= kopia:
        kmax += 1
        max = silnia(kmax)
    max //= kmax
    kmax -= 1
    if n == max:
        return 1
    tablica = []
    for i in range(0, n):
        tablica.append(0)
    while suma != n:
        suma = silnia(tablica[0]) + silnia(tablica[1])


n = int(input("Podaj liczbę: "))
print(liczba_silna(n))