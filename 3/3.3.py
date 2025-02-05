def bmi(masa, wzrost):
    return masa / (wzrost ** 2)


masa = float(input("Podaj masę w kg: "))
wzrost = float(input("Podaj wzrost w m: "))
if bmi(masa, wzrost) < 18.5:
    print("Masz niedowagę")
elif bmi(masa, wzrost) >= 25:
    print("Masz nadwagę")
else:
    print("Twoja waga jest prawidłowa")
