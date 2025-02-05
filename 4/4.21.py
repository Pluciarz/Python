def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

def podwojna_silnia(n):
    wynik = 1
    while n > 0:
        wynik *= n
        n -= 2
    return wynik

n = int(input("Podaj liczbę: "))
print("Silnia z", n, "wynosi", silnia(n))
print("Podwójna silnia z", n, "wynosi", podwojna_silnia(n))
