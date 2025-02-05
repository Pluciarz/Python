import random

def wypelnianie():
    tablica = []
    for i in range(50):
        tablica.append(random.randint(1, 100))
    return tablica

def szukanie(n):
    tablica = wypelnianie()
    x = -1
    tablica.append(x)
    i = 0
    while tablica[i] != n:
        i += 1
        if tablica[i] == x:
            tablica.pop()
            return print("Tablica"), print(", ".join(map(str, tablica))), print("W tablicy nie ma szukanej wartości")
    tablica.pop()
    return print("Tablica"), print(", ".join(map(str, tablica))), print("Znaleziono wartość na indeksie", i)

n = int(input("Podaj szukaną liczbę(1 - 100): "))
szukanie(n)