def potega(p, w):
    wynik = 1
    while w > 0:
        wynik *= p
        w -= 1
    return wynik

def ile_cyfr(n):
    ile = 0
    while n > 0:
        ile += 1
        n //= 10
    return ile

def czy_armstronga(n):
    kopia = n
    suma = 0
    while n > 0:
        suma += potega(n % 10, ile_cyfr(kopia))
        n //= 10
    if kopia == suma:
        return True
    return False

n = int(input("Podaj liczbę: "))
if (czy_armstronga(n) == True):
    print("Liczba", n, "jest liczbą Armstronga")
else:
    print("Liczba", n, "nie jest liczbą Armstronga")