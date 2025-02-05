tekst = input("Podaj słowo: ")
odwrotnie = tekst[::-1]
if tekst.lower() == odwrotnie.lower():
    print("Podane słowo jest palindromem")
else:
    print("Podane słowo nie jest palindromem")