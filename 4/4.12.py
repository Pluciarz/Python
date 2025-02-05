import random

x = int(input("Podaj liczbę losowanych liczb: "))
suma = 0
print("Wylosowane liczby: ")
for i in range(x):
    a = random.randint(10, 99)
    print(a)
    suma += 1 / a
srednia = x / suma
print("Średnia harmoniczna wylosowanych liczb wynosi:", srednia)
