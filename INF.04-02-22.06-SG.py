class Osoba:

    liczba_instancji = 0

    def __init__(self, nome = "", id = 0):
        self.__id = id
        self.__nome = nome
        Osoba.liczba_instancji += 1

    def copy_from(self, other):
        self.__id = other.__id
        self.__nome = other.__nome
        Osoba.liczba_instancji += 1

    def greet(self, other_nome):
        if self.__nome == "":
            print("brak danych")
        else:
            print("Cześć" + other_nome + "mam na imie", self.__nome)

    def show(self):
        print("ID: " + str(self.__id) + "|  Nome: " + self.__nome)


def main():
    o1 = Osoba()
    o1.show()

    o2 = Osoba("ala", 1)
    o2.show()

    o3 = Osoba()
    o3.copy_from(o2)
    o3.show()

    o2.greet("JAN")
    o1.greet("JAN")

    print("Liczba instancji: " + str(Osoba.liczba_instancji))

if __name__ == "__main__":
    main()