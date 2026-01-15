import random

def losuj_tablice():
    tablica = []
    for i in range(100):
        tablica.append(random.randint(1, 100))

    return tablica

def bumble_sort(tablica):
    for i in range(100):
        for j in range(100):
            if tablica[i] < tablica[j]:
                tablica[i], tablica[j] = tablica[j], tablica[i]

def wypisz(tablica):
    wynik = ""
    for i in range(100):
        wynik += str(tablica[i]) + ", "
    print(wynik)

def main():
    tablica = losuj_tablice()
    bumble_sort(tablica)
    wypisz(tablica)

if __name__ == "__main__":
    main()