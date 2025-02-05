import random

x = None
suma = 0
while x != 6:
    suma += 1
    x = random.randint(1, 6)
    print(suma, "wylosowana liczba:", x)
print("Liczba 6 została wylosowana za", suma, "razem")