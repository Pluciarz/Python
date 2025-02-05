import string

tekst = input("Podaj tekst: ")
tekst_bez_interpunkcji = tekst.translate(str.maketrans("", "", string.punctuation))
print("Tekst bez interpunkcji:", tekst_bez_interpunkcji)