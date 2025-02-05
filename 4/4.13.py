def czy_pierwsza(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return 0
    return 1


def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


def rozklad(n):
    suma = 0
    czynnik = 2
    while n > 1:
        if n % czynnik == 0:
            suma += suma_cyfr(czynnik)
            n //= czynnik
        else:
            czynnik += 1
    return suma


print("Wszystkie trzycyfrowe liczby Smitha:")
for i in range(100, 1000):
    if czy_pierwsza(i) == 0 and rozklad(i) == suma_cyfr(i):
        print(i)
