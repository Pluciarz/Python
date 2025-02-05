def NWD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
print("NWD(", a, ",", b, ") =", NWD(a, b))