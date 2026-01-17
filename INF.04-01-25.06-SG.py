import random


def losuj(ile, losowania):
    for i in range(ile):
        zestaw = random.sample(range(1, 49), 6)
        losowania.append(zestaw)

def wypisz(ile, losowania):
    for i in range(ile):
        print("Losowanie", str(i) + ":")
        for j in losowania[i]:
            print(j, end=" ")
        print(end="\n")

def wystapienia(losowania):

    for i in range(1, 49):
        print("Wystąpienia liczby", str(i) + ":")
        wynik = 0
        for j in losowania:
            if i in j:
                wynik += 1
        print(wynik, end="\n")


def main():
    ile = int(input("Podaj ile: "))

    losowania = []
    losuj(ile, losowania)

    wypisz(ile, losowania)

    wystapienia(losowania)


if __name__ == "__main__":
    main()