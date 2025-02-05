slowo = input("Podaj słowo: ")
szyfr = ""
for i in slowo:
    szyfr += chr(ord(i) + 13)
print("Słowo", slowo, "zaszyfrowane w ROT13 wygląda tak:", szyfr)