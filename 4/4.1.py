def funkcja(a, b, x):
    return a * x + b


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
k = int(input("Podaj koniec przedziału: "))
print("Wartości funkcji:")
for x in range(1, k + 1):
    if x % 2 == 0:
        print("f(", x, ") =", funkcja(a, b, x))
