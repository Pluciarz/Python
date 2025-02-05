import math
def delta(a, b, c):
    return b ** 2 - 4 * a * c
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if a == 0:
    print("Nie można obliczyć delty")
elif delta(a, b, c) > 0:
    x1 = (-b - math.sqrt(delta(a, b, c))) / 2 * a
    x2 = (-b + math.sqrt(delta(a, b, c))) / 2 * a
    print("Podana funkcja ma 2 miejsca zerowe: x1 =", x1, ", x2 =", x2)
elif delta(a, b, c) == 0:
    x = -b / 2 * a
    print("Podana funkcja ma 1 miejsce zerowe: x =", x)
else:
    print("Podana funkcja nie posiada miejsc zerowych")