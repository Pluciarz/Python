slowo = input("Podaj słowo: ")
znak = input("Podaj znak: ")
print("Znak", znak, "występuje w słowie", slowo, "w tylu procentach:", slowo.lower().count(znak.lower()) / len(slowo) * 100)