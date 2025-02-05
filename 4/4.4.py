def suma_cyfr(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma


def iloscCyfr(x):
    ile = 0
    while x > 0:
        ile += 1
        x //= 10
    return ile


x = int(input("Podaj liczbę: "))
print("Suma cyfr:", suma_cyfr(x))
print("Ilość cyfr:", iloscCyfr(x))
if x % suma_cyfr(x) == 0:
    print("Podana liczba jest liczbą Nivena")
else:
    print("Podana liczba nie jest liczbą Nivena")
