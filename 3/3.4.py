def funkcja(a, b, c, x):
    return a * (x ** 2) + b * x + c


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
x = int(input("Podaj x: "))
print("Wartość funkcji: ", funkcja(a, b, c, x))
if a == 0:
    print("Funkcja jest liniowa")
