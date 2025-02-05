def funkcja(a, b, c, x):
    return a * (x ** 2) + b * x + c


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
k = int(input("Podaj koniec przedziału: "))
x = 1
print("Wartości funkcji:")
while x < k + 1:
    if x % 2 != 0:
        print("f(", x, ") =", funkcja(a, b, c, x))
    x += 1
