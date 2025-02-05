def ile_cyfr(n):
    ile = 0
    while n > 0:
        ile += 1
        n //= 10
    return ile


def potegi_cyfr(n):
    suma = 0
    wykladnik = ile_cyfr(n)
    while n > 0:
        suma += (n % 10) ** wykladnik
        n //= 10
    return suma


n = int(input("Podaj liczbę: "))
if n == potegi_cyfr(n):
    print("Liczba", n, "jest liczbą Armstronga")
else:
    print("Liczba", n, "nie jest liczbą Armstronga")
print("Wszystkie 3, 4 i 5-cyfrowe liczby Armstronga:")
for i in range(100, 100000):
    if i == potegi_cyfr(i):
        print(i)
