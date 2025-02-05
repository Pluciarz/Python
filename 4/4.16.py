def NWD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
def NWW(a, b):
    return (a * b) // NWD(a, b)

a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
print("NWW(", a, ",", b, ") =", NWW(a, b))