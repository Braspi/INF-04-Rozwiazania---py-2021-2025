import random

def fill_table():
    table = []
    for i in range(50):
        table.append(random.randint(1, 100))
    return table

def sentinel_search(table, x):
    n = len(table)

    table.append(x)

    i = 0
    while table[i] != x:
        i += 1

    table.pop()

    if i < n:
        return i
    else:
        return -1

def print_table(table):
    print("Tablica:")
    for i in range(50):
        print(table[i], end=", ")
    print()

def main():
    table = fill_table()

    x = int(input("Podaj liczbę do wyszukania"))

    index = sentinel_search(table, x)
    print_table(table)

    if index == -1:
        print("Niestety nie ma")
    else:
        print("Znaleniono na indexie", index)


if __name__ == '__main__':
    main()