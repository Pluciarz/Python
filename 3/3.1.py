a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
    print("Trójkąt jest prostokatny")
else:
    print("Trójkąt nie jest prostokątny")
