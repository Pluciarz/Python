def fibbonacci(n):
    a = 0
    b = 1
    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return a

n = int(input("Podaj liczbę: "))
print(n, "wyraz ciągu Fibbonacciego wynosi", fibbonacci(n))