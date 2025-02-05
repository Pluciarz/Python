import random

losowania = []
for i in range (0, 10):
    losowania.append(random.randint(1, 100))
min = 100
max = 0
suma = 0
for liczba in losowania:
    suma += 1 / liczba
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba
print("Wartość maksymalna:", max)
print("Wartość minimalna:", min)
srednia = 10 / suma
print("Średnia harmoniczna:", srednia)