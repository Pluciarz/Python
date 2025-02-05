tekst = input("Podaj tekst: ")
litery = 0
cyfry = 0
for i in tekst:
    if i.isalpha():
        litery += 1
    if i.isdigit():
        cyfry += 1
print("W tekście", tekst, "jest tyle liter:", litery, "i tyle cyfr:", cyfry)