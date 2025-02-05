def iteracyjnie(n):
    wynik = 1
    while n > 0:
        wynik *= n
        n -= 2
    return wynik

def rekurencyjnie(n):
    if n == 0 or n == 1:
        return 1
    return n * rekurencyjnie(n - 2)

n = int(input("Podaj liczbę: "))
print(n, "silnia iteracyjnie wynosi,", iteracyjnie(n))
print(n, "silnia rekurencyjnie wynosi", rekurencyjnie(n))