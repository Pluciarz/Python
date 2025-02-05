def pole(r):
    return round(3.14 * r ** 2, 3)
def obwod(r):
    return round(6.28 * r, 3)
r = int(input("Podaj promień: "))
print("Pole koła:", pole(r))
print("Obwód koła:", obwod(r))