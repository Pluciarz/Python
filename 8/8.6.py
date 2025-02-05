import math

def znajdz_pierwsze(n):
    if n <= 1:
        print("n musi być liczbą całkowitą większą niż 1")

    # Inicjalizacja tablicy wartości logicznych
    A = [True] * (n + 1)

    # Implementacja algorytmu sita Eratostenesa
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i]:  # Jeśli A[i] = True
            for j in range(i * i, n + 1, i):
                A[j] = False

    # Wyjście: indeksy, dla których A[i] = True
    return [i for i in range(2, n + 1) if A[i]]

n = 100
pierwsze_liczby = znajdz_pierwsze(n)
print(pierwsze_liczby)
