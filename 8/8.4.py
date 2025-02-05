# Funkcja do sprawdzania poprawności numeru NIP
def sprawdz_nip(nip):
    if len(nip) != 10 or not nip.isdigit():
        return False
    wagi = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    suma_kontrolna = sum(w * int(n) for w, n in zip(wagi, nip[:9])) % 11
    return suma_kontrolna == int(nip[-1])


def main():
    firmy = []
    unikalne_nipy = set()
    n = int(input("Podaj liczbę firm do wprowadzenia: "))

    for _ in range(n):
        print("\nWprowadzanie danych o firmie:")
        nip = input("Podaj NIP: ")
        if not sprawdz_nip(nip):
            print("Niepoprawny numer NIP. Spróbuj ponownie.")
            continue
        if nip in unikalne_nipy:
            print("Firma z tym NIP-em już istnieje.")
            continue

        nazwa = input("Podaj nazwę firmy: ")
        adres = input("Podaj miasto: ")
        rok_zalozenia = int(input("Podaj rok założenia: "))

        firmy.append({
            "NIP": nip,
            "nazwa": nazwa,
            "adres": adres,
            "rok_zalozenia": rok_zalozenia
        })
        unikalne_nipy.add(nip)

    # Analiza danych
    gdańsk_10_lat = [
        firma for firma in firmy
        if firma["adres"].lower() == "gdańsk" and (2024 - firma["rok_zalozenia"]) >= 10
    ]
    print(f"\nLiczba firm w Gdańsku, które istnieją od minimum 10 lat: {len(gdańsk_10_lat)}")


if __name__ == "__main__":
    main()
