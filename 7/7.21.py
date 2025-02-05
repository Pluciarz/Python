slowo = input("Podaj słowo: ")
for i in range (len(slowo)):
    if i % 2 == 0:
        print(slowo[i], end = " ")