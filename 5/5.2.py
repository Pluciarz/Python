def silnia(n):
    if n== 0 or n == 1:
        return 1
    return n * silnia(n - 1)

def podwojna_silnia(n):
    if n == 0 or n == 1:
        return 1
    return n * podwojna_silnia(n - 2)

def potrojna_silnia(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return n * potrojna_silnia(n - 3)

def k_silnia(n, k):
    if n == 0:
        return 1
    if n > 0 and n <= k:
        return n
    return n * k_silnia(n - k, k)

n = int(input("Podaj liczbę: "))
k = int(input("Podaj stopień silni: "))
print("Silnia z", n, "wynosi", silnia(n))
print("Podwójna silnia z", n, "wynosi", podwojna_silnia(n))
print("Potrójna silnia z", n, "wynosi", potrojna_silnia(n))
print("Silnia o stopniu", k, "z", n, "wynosi", k_silnia(n, k))