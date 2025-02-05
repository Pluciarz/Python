def czy_pierwsza(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

parzyste = 0
nieparzyste = 0
for i in range(1, 1001):
    if czy_pierwsza(i) and i ** 2 <= 1000:
        potega = i ** 2
        print(potega)
        if potega % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1
print("Liczb parzystych jest", parzyste)
print("Liczb nieparzystych jest", nieparzyste)