slowo1 = input("Podaj słowo: ")
slowo2 = input("Podaj słowo: ")
if sorted(slowo1.lower()) == sorted(slowo2.lower()):
    print("Podane słowa są anagramami")
else:
    print("Podane słowa nie są anagramami")