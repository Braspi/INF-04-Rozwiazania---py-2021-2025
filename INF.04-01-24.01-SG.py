import sys


def check_plec(pesel):
    if int(pesel[9]) % 2 == 0:
        return 'K'
    else:
        return 'M'

def suma_kontrolna(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9,1,3]

    suma = 0

    for i in range(len(pesel) -1):
        suma += int(pesel[i]) * wagi[i]

    m = suma % 10

    if m == 0:
        r = 0
    else:
        r = 10 - m

    return r == int(pesel[10])

def main():
    pesel_zdajacego = int(00000000000)
    pesel = input("Podaj pesel: ")

    if len(pesel) == 11:
        plec = check_plec(pesel)
        if plec == 'K':
            print("Kobieta")
        elif plec == 'M':
            print("Mężczyzna")

        wynik_opertacji = suma_kontrolna(pesel)

        if wynik_opertacji:
            print("poprawna suma kontrolna")
        else:
            print("nie poprawna suma kontrolna")
    else:
        print("Pesel nie jest poprawny")


if __name__ == "__main__":
    main()
