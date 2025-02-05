tekst = input("Podaj tekst: ")
litery = 0
cyfry = 0
for i in tekst:
    if i.isalpha():
        litery += ord(i)
    if i.isdigit():
        cyfry += ord(i)
print("W tekście", tekst, "suma kodów ASCII liter wynosi:", litery, ", a cyfr:", cyfry)