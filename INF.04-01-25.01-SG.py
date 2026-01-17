import random


class Tablice:
    def __init__(self, rozmair_tablicy):
        self.rozmair_tablicy = rozmair_tablicy
        self.tablica = []

        for i in range(rozmair_tablicy):
            self.tablica.append(random.randint(1, 1000))

        print(self.tablica)

    def wypisz(self):
        for i in range(self.rozmair_tablicy):
            print(str(i) + ":", self.tablica[i])

    def szukaj(self, szukana):
        for i in range(self.rozmair_tablicy):
            if szukana == self.tablica[i]:
                return i
        return -1

    def nie_parzyste(self):
        counter = 0

        for i in range(self.rozmair_tablicy):
            if self.tablica[i] % 2 != 0:
                print(self.tablica[i])
                counter += 1

        print("Razem nieparzystych: ", counter)

    def licz_artm(self):

        wynik = 0

        for i in range(self.rozmair_tablicy):
            wynik += self.tablica[i]

        return wynik % self.rozmair_tablicy

def main():
    x = int(input("podaj rozmiar tablica: "))

    tab = Tablice(x)

    tab.wypisz()

    wartosc = int(input("Podaj szukną: "))
    szukana = tab.szukaj(wartosc)

    if szukana == -1:
        print("Nie znaleziono")
    else:
        print("Znaleziono na index: " + str(szukana))

    tab.nie_parzyste()

    print("Średnia wszytskich elementów: " + str(tab.licz_artm()))

if __name__ == "__main__":
    main()