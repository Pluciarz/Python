def suma_dzielnikow(n):
    suma = 0
    czynnik = 1
    while czynnik < n:
        if n % czynnik == 0:
            suma += czynnik
        czynnik += 1
    return suma


a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
if a != 1 and b != 1:
    if suma_dzielnikow(a) - 1 == b and suma_dzielnikow(b) - 1 == a:
        print("Podane liczby są skojarzone")
    else:
        print("Podane liczby nie są skojarzone")
else:
    print("Żadna z liczb nie może być równa 1")
