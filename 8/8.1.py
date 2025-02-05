wyjatki = {
    "hard":"hard",
    "late":"late",
    "fast":"fast",
    "cold":"cold",
    "small":"small",
    "high":"high",
    "good":"well"
}
przymiotnik = input("Podaj przymiotnik w j.angielskim: ")
if przymiotnik in wyjatki:
    przyslowek = wyjatki[przymiotnik]
elif przymiotnik.endswith("le"):
    przyslowek = przymiotnik[:len(przymiotnik) - 1] + "y"
elif przymiotnik.endswith("y"):
    przyslowek = przymiotnik[:len(przymiotnik) - 1] + "ily"
elif przymiotnik.endswith("ic"):
    przyslowek = przymiotnik + "ally"
else:
    przyslowek = przymiotnik + "ly"
print("Przysłówek utworzyny z przymiotnika:", przymiotnik, "wygląda następująco:", przyslowek)