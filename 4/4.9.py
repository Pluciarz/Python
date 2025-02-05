import random


def czy_pierwsza(n):
    ile = 0
    for i in range(2, n // 2):
        if n % i == 0:
            ile += 1
    return ile


x = random.randint(1, 100)
if czy_pierwsza(x) == 0:
    print("Wylosowana liczba", x, "jest liczbą pierwszą")
else:
    print("Wylosowana liczba", x, "nie jest liczbą pierwszą")
