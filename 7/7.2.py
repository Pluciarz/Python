tekst = input("Podaj tekst: ")
slowo = input("Podaj słowo: ")
if slowo.lower() in tekst.lower():
    print(slowo, "jest w tekście", tekst)
else:
    print(slowo, "nie jest w tekście", tekst)