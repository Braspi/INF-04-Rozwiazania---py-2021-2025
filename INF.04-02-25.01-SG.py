class Agd():
    def __init__(self, text):
        self.text = text
        print(text)


class Pralka(Agd):
    def __init__(self):
        self.__numer_prania = 0

    def set_numer_prania(self, numer_prania):
        if 1 < self.__numer_prania > 10:
            self.__numer_prania = numer_prania
            Agd("Program został ustawiony")
        else:
            self.__numer_prania = 0

        return self.__numer_prania

    def print_on(self):
        Agd("Odkurzacz włączono")

    def print_off(self):
        Agd("Odkurzacz włączono")

class Odkurzacz(Pralka):
    def __init__(self):
        self.__stan_odkurzacza = False

    def on(self):
        if not self.__stan_odkurzacza:
            self.__stan_odkurzacza = True
            self.print_on()

    def off(self):
        if self.__stan_odkurzacza:
            self.__stan_odkurzacza = False
            self.print_off()

def main():
    pralka = Pralka()
    odkurzacz = Odkurzacz()

    nr = int(input("Podaj numer prania: "))

    pralka.set_numer_prania(nr)
    odkurzacz.on()
    odkurzacz.on()
    odkurzacz.on()
    Agd("Odkurzacz wyładował się")
    odkurzacz.print_off()


if __name__ == "__main__":
    main()

