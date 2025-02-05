import math


def iteracyjnie(n):
    x1 = 0
    x2 = 1
    if n == 0:
        return x1
    if n == 1:
        return x2
    i = 2
    while i <= n:
        kopia = x2
        x2 += x1
        x1 = kopia
        i += 1
    return x2

def rekurencyjnie(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rekurencyjnie(n - 1) + rekurencyjnie(n - 2)

def potega(p, w):
    if w == 0:
        return 1
    return p * potega(p, w - 1)

def wzorBineta(n):
    return (1 / math.sqrt(5)) * potega((1 + math.sqrt(5)) / 2, n)

n = int(input("Podaj liczbę: "))
print(n, "wyraz ciągu Fibonacciego iteracyjnie:", iteracyjnie(n))
print(n, "wyraz ciągu Fibonacciego rekurencyjnie:", rekurencyjnie(n))
print(n, "wyraz ciągu Fibonacciego wzorem Bineta:", wzorBineta(n))