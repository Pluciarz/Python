def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def tri(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tri(n - 1) + tri(n - 2) + tri(n - 3)

def tetra(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    if n == 3:
        return 1
    return tetra(n - 1) + tetra(n - 2) + tetra(n - 3) + tetra(n - 4)

def luc(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return luc(n - 1) + luc(n - 2)

n = int(input("Podaj liczbę: "))
print(n, "wyraz ciągu Fibonacciego wynosi", fib(n))
print(n, "wyraz ciągu Tribonacciego wynosi", tri(n))
print(n, "wyraz ciągu Tetranacciego wynosi", tetra(n))
print(n, "wyraz ciągu Lucasa wynosi", luc(n))